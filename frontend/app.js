const chatWindow = document.getElementById('chat-window');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');

function addMessage(content, isUser = false, isJSON = false) {
    const msgDiv = document.createElement('div');
    msgDiv.classList.add('message');
    msgDiv.classList.add(isUser ? 'user-message' : 'bot-message');

    if (isJSON) {
        msgDiv.innerHTML = formatJSONOutput(content);
    } else {
        msgDiv.textContent = content;
    }

    chatWindow.appendChild(msgDiv);
    chatWindow.scrollTop = chatWindow.scrollHeight;
}

function formatJSONOutput(data) {
    if (!data.cases) return `<p>${JSON.stringify(data)}</p>`;

    let html = `<div class="test-suite-container">
        <h3 style="margin-bottom: 12px; color: #fff;">📋 ${data.test_suite || 'Generated Test Suite'}</h3>`;

    data.cases.forEach(c => {
        html += `<div class="test-case">
            <h4>${c.id}: ${c.title}</h4>
            <ul>
                ${c.steps.map(s => `<li>${s}</li>`).join('')}
            </ul>
            <p style="margin-top: 8px; font-size: 0.85rem;">
                <strong style="color: #10b981;">Expected:</strong> ${c.expected}
            </p>
        </div>`;
    });

    html += `</div>`;
    return html;
}

async function handleSend() {
    const text = userInput.value.trim();
    if (!text) return;

    // Clear input
    userInput.value = '';

    // Add User Message
    addMessage(text, true);

    // Add Loading State
    const loadingDiv = document.createElement('div');
    loadingDiv.classList.add('message', 'bot-message', 'loading-msg');
    loadingDiv.innerHTML = `<div class="loading-dots">
        <div class="dot"></div>
        <div class="dot"></div>
        <div class="dot"></div>
    </div>`;
    chatWindow.appendChild(loadingDiv);
    chatWindow.scrollTop = chatWindow.scrollHeight;

    try {
        const response = await fetch('/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ requirement: text })
        });

        const data = await response.json();

        // Remove Loading
        chatWindow.removeChild(loadingDiv);

        if (response.ok) {
            addMessage(data, false, true);
        } else {
            addMessage(`Error: ${data.detail || 'Something went wrong.'}`);
        }
    } catch (error) {
        chatWindow.removeChild(loadingDiv);
        addMessage(`Connection error: Unable to reach the backend.`);
    }
}

sendBtn.addEventListener('click', handleSend);
userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') handleSend();
});
