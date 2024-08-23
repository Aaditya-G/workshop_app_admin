const bigContainer = document.getElementById("big-container");

async function getPosts() {
    try {
        const response = await fetch("http://127.0.0.1:5000/api/messages");
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        appendPosts(data);
    } catch (error) {
        console.error('Error fetching approved messages:', error);
        displayError("Failed to load messages. Please try again later.");
    }
}

function appendPosts(messages) {
    bigContainer.innerHTML = ''; // Clear existing content

    if (messages.length === 0) {
        displayNoMessages();
    } else {
        messages.forEach(message => {
            const div = document.createElement("div");
            const h6 = document.createElement("h6");
            const p = document.createElement("p");
            
            h6.textContent = message.content;
            p.textContent = message.username;
            
            div.appendChild(h6);
            div.appendChild(p);
            div.classList.add("card");
            bigContainer.appendChild(div);
        });
    }
}

function displayNoMessages() {
    const p = document.createElement("p");
    p.textContent = "No posts to display yet!";
    p.classList.add("no-messages");
    bigContainer.appendChild(p);
}

function displayError(message) {
    const errorDiv = document.createElement("div");
    errorDiv.textContent = message;
    errorDiv.classList.add("error-message");
    bigContainer.appendChild(errorDiv);
}

window.addEventListener("load", getPosts);