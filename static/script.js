async function predictResult() {
    const hoursInput = document.getElementById('studyHours');
    const resultContainer = document.getElementById('result');
    const predictionText = document.getElementById('predictionText');
    const probabilityText = document.getElementById('probabilityText');

    const hours = hoursInput.value;

    if (hours === '' || hours < 0) {
        alert('Please enter a valid number of study hours.');
        return;
    }

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ hours: hours })
        });

        const data = await response.json();

        if (response.ok) {
            resultContainer.classList.remove('hidden');
            predictionText.innerText = data.result;
            probabilityText.innerText = data.probability;

            // Remove old classes
            predictionText.classList.remove('pass', 'fail');

            // Add new class based on result
            if (data.result === 'Pass') {
                predictionText.classList.add('pass');
            } else {
                predictionText.classList.add('fail');
            }
        } else {
            alert('Error: ' + data.error);
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Failed to get prediction. Make sure the server is running.');
    }
}
