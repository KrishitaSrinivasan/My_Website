//Makes JavaScript more sensitive to errors so it is easier to debug in the future
'use strict';
//helps select the variable button
const switcher = document.body.querySelector('.btn');
//helps conduct the click function
switcher.addEventListener('click', function() {
     //helps to toggle the light-theme class in the body
    document.body.classList.toggle('light-theme');
    //helps to toggle the dark-theme class in the body
    document.body.classList.toggle('dark-theme');
    const className = document.body.className;
    if (document.body.classList.contains("light-theme")) {
  this.textContent = "Dark";
} else {
  this.textContent = "Light";
}

});
document.addEventListener("DOMContentLoaded", () => {
  const items = document.querySelectorAll(".sidenav a");

  items.forEach(item => {
    item.addEventListener("mouseenter", () => {
      item.style.transform = "translateY(-6px) scale(1.08)";
    });

    item.addEventListener("mouseleave", () => {
      item.style.transform = "translateY(0) scale(1)";
    });
  });
});
async function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value.trim();
    if (message === "") return;

    addUserMessage(message);
    input.value = "";

    const response = await fetch("YOUR_BACKEND_URL_HERE", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: message })
    });

    const data = await response.json();
    addBotMessage(data.reply);
}

function addUserMessage(text) {
    const box = document.getElementById("chat-box");
    box.innerHTML += `<div class="user-message">${text}</div>`;
    box.scrollTop = box.scrollHeight;
}

function addBotMessage(text) {
    const box = document.getElementById("chat-box");
    box.innerHTML += `<div class="bot-message">${text}</div>`;
    box.scrollTop = box.scrollHeight;
}
