function sendCommand() {
    const command = document.getElementById('commandInput').value.trim();
    if (!command) {
        document.getElementById('response').innerText = "Please enter or speak a command.";
        return;
    }
    document.getElementById('response').innerText = "Processing...";
    fetch('/process', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ command: command })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('response').innerText = data.response;
    })
    .catch(() => {
        document.getElementById('response').innerText = "Error connecting to assistant.";
    });
}

function startListening() {
    if (!('webkitSpeechRecognition' in window)) {
        alert('Speech recognition not supported in this browser.');
        return;
    }
    const recognition = new webkitSpeechRecognition();
    recognition.lang = 'en-US';
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;

    const micBtn = document.getElementById('micBtn');
    const micIcon = document.getElementById('micIcon');
    micBtn.classList.add('mic-anim');
    micIcon.textContent = "🔴";

    recognition.onresult = function(event) {
        const transcript = event.results[0][0].transcript;
        document.getElementById('commandInput').value = transcript;
        micBtn.classList.remove('mic-anim');
        micIcon.textContent = "🎤";
        sendCommand();
    };

    recognition.onerror = function(event) {
        micBtn.classList.remove('mic-anim');
        micIcon.textContent = "🎤";
        document.getElementById('response').innerText = 'Speech recognition error: ' + event.error;
    };

    recognition.onend = function() {
        micBtn.classList.remove('mic-anim');
        micIcon.textContent = "🎤";
    };

    recognition.start();
}

// Allow pressing Enter to send command
document.getElementById('commandInput').addEventListener('keydown', function(e) {
    if (e.key === 'Enter') sendCommand();
});
// Register service worker for PWA support
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/static/service-worker.js');
}