document.addEventListener('DOMContentLoaded', function() {
    const quizForm = document.getElementById('quiz-form');
    const timerDisplay = document.getElementById('timer');
    const questionContainer = document.getElementById('question-container');
    const resultContainer = document.getElementById('result-container');
    const scoreDisplay = document.getElementById('score');
    let currentQuestionIndex = 0;
    let score = 0;
    let timer;

    function startTimer() {
        let timeLeft = 60;
        timerDisplay.textContent = timeLeft;

        timer = setInterval(function() {
            timeLeft--;
            timerDisplay.textContent = timeLeft;

            if (timeLeft <= 0) {
                clearInterval(timer);
                submitAnswer();
            }
        }, 1000);
    }

    function showQuestion() {
        const question = quizData[currentQuestionIndex];
        questionContainer.innerHTML = `
            <h2>${question.question}</h2>
            <div>
                <input type="radio" name="answer" value="${question.option1}" id="option1">
                <label for="option1">${question.option1}</label>
            </div>
            <div>
                <input type="radio" name="answer" value="${question.option2}" id="option2">
                <label for="option2">${question.option2}</label>
            </div>
            <div>
                <input type="radio" name="answer" value="${question.option3}" id="option3">
                <label for="option3">${question.option3}</label>
            </div>
            <div>
                <input type="radio" name="answer" value="${question.option4}" id="option4">
                <label for="option4">${question.option4}</label>
            </div>
        `;
        startTimer();
    }

    function submitAnswer() {
        clearInterval(timer);
        const selectedAnswer = document.querySelector('input[name="answer"]:checked');

        if (selectedAnswer) {
            if (selectedAnswer.value === quizData[currentQuestionIndex].answer) {
                score++;
            }
        }

        currentQuestionIndex++;

        if (currentQuestionIndex < quizData.length) {
            showQuestion();
        } else {
            showResult();
        }
    }

    function showResult() {
        questionContainer.style.display = 'none';
        resultContainer.style.display = 'block';
        scoreDisplay.textContent = `Your score: ${score} / ${quizData.length}`;
    }

    quizForm.addEventListener('submit', function(event) {
        event.preventDefault();
        submitAnswer();
    });

    showQuestion();
});