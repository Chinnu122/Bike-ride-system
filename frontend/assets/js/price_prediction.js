document.getElementById('prediction-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const pickup = document.getElementById('pickup').value;
    const drop = document.getElementById('drop').value;
    const time = document.getElementById('time').value;

    const response = await fetch('/api/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ pickup, drop, time })
    });
    const data = await response.json();
    document.getElementById('result').innerText = `Predicted Price: ${data.price}`;
});
