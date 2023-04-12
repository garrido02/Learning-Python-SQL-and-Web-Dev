//part 1
document.addEventListener('DOMContentLoaded', function() {

    //create variable for feedback
    let feedback1 = document.querySelector('#feedback1');

    //create variable for correct
    let correct = document.querySelector('.correct');

    //if correct is clicked then we want a text to appear and button change color
    correct.addEventListener("click", function(right) {
        correct.style.backgroundColor = 'green';
        feedback1.innerHTML = 'Correct!';
        feedback1.style.color = 'green';
    })

    //create variable for incorrect and for that feedback
    let incorrect = document.querySelectorAll('.incorrect');

    //if wrong awnser is giving we want text to appear red and button change color
    for (let i = 0; i < incorrect.length; i++) {
        incorrect[i].addEventListener('click', function(wrong) {
            incorrect[i].style.backgroundColor = 'red';
            feedback1.innerHTML = 'Incorrect!';
            feedback1.style.color = 'red';
        })
    }


// part 2

    //create correct variables and feedback 2 variables based on file
    let input = document.querySelector('input');
    let submit = document.querySelector('#submit');
    let feedback2 = document.querySelector('#feedback2');

    //check if input is equal to the expected awnser and make sure is case insensitive
    submit.addEventListener('click', function(check) {
        if (input.value.toLowerCase() === 'Fellowship of the Ring'.toLowerCase())
        {
            input.style.backgroundColor = 'green';
            feedback2.innerHTML = 'Correct!';
            feedback2.style.color = 'green';
        }

        else
        {
            input.style.backgroundColor = 'red';
            feedback2.innerHTML = 'Incorrect!';
            feedback2.style.color = 'red';
        }
    })
})

