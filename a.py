import sys
sys.path.append(f'c:\python38\lib\site-packages')
import requests

from time import sleep
from pathlib import Path


api_key = "0457f35f91c5260b0ddb1d79a3065c08efe85d858c35d9158a2cb981998ded50"

def scan_file(api_key, file_path):
    with open(file_path, "rb") as data:
        url = 'https://www.virustotal.com/vtapi/v2/file/scan'

        params = {'apikey': api_key}

        files = {"file": data}
        response = requests.post(url, files= files, params = params)
      #  print(response)

        return get_report(api_key, response.json()["resource"])


def get_report(api_key, resourceId):
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    params = {"apikey": api_key, "resource": resourceId}
    while True:
        try:
            r = requests.get(url, params=params)
            if r.status_code != requests.codes.ok:
                return
            r.raise_for_status()  # Raise an error for bad responses (e.g., 404)
            report = r.json()
            if report['response_code'] == 1:
                return report

            delay = 7
            # Adjust delay time as needed
            print(f'Retrying in {delay} seconds...')
            sleep(delay) 
        except Exception as e:
            print(e)
           
def scan_directory(path):
    # itme is file:

    if path.is_file():
        response = scan_file(api_key, path)
        try:
            positives = response["positives"]
            if positives == 0:
                print(f"File {path} is good (not detected as malicious).")
            else:
                print(f"File {path} is flagged by {positives} antivirus engines.")
        except Exception as e:
            return
    else:
        for item in path.iterdir():
            scan_directory(item)

def main():

    directory_path = Path(input("enter folder/file to start with: "))

    scan_directory(directory_path)


if __name__ == "__main__":
    main()