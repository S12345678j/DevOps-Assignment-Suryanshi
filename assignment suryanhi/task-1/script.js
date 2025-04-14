// Load messages when page loads
window.onload = () => {
    fetchMessages();
};

function fetchMessages() {
    fetch('/api/messages')
        .then(response => response.json())
        .then(data => {
            const list = document.getElementById('messages-list');
            list.innerHTML = '';
            data.forEach(msg => {
                const li = document.createElement('li');
                li.textContent = msg.content;
                list.appendChild(li);
            });
        });
}

function sendMessage() {
    const input = document.getElementById('message-input');
    const content = input.value;

    if (!content) return;

    fetch('/api/messages', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ content: content })
    })
    .then(response => response.json())
    .then(() => {
        input.value = '';
        fetchMessages(); 
    });
}
