// Toggle theme and update button text
function toggleTheme() {
    document.body.classList.toggle("dark-mode");
    updateButtonText();
}

// Update button label based on current theme
function updateButtonText() {
    const btn = document.getElementById("theme-toggle");
    if (document.body.classList.contains("dark-mode")) {
        btn.innerText = "Switch to Light Mode";
    } else {
        btn.innerText = "Switch to Dark Mode";
    }
}

// Add button on page load
window.onload = function() {
    const btn = document.createElement("button");
    btn.id = "theme-toggle";
    document.body.appendChild(btn);
    btn.onclick = toggleTheme;
    updateButtonText();
};