document.getElementById('userAnswer').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        checkAnswer();
    }
});


function checkAnswer() {
    var userAnswer = document.getElementById('userAnswer').value.trim().toLowerCase();
    var possibleAnswers = ["צל", "חושך"];

    if (possibleAnswers.includes(userAnswer)) {
        window.location.href = "win.html"; // Redirect to win page if answer is correct
    } else {
        document.getElementById('result').innerText = "יגרוע בכלל!";
        document.getElementById('result').style.color = "#dc3545"; // Red color for incorrect answer
    }
}

function backToMain() {
    window.location.href = "index.html";
}

function changeName(element) {
    element.textContent = 'דנאל'; // Change the text content to "Danel"
    var nameBoxes = document.getElementsByClassName('name-box');
    var all_danel = true;
    for (var i = 0; i < nameBoxes.length; i++) {
        if(nameBoxes[i].innerText != 'דנאל')
        {
            all_danel = false;
        } // This will log each element with the class 'name-box'
    }
    if (all_danel) {
        window.location.href = "final_win.html"; // Redirect to win page if answer is correct
    } 
}

function backToMain() {
    window.location.href = "index.html"; // Redirect to the main page
}
