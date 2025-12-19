function toggleTheme() {
    document.body.classList.toggle("dark-mode");
    updateToggleLabel();
}

function updateToggleLabel() {
    const label = document.getElementById("theme-label");
    label.innerText = document.body.classList.contains("dark-mode") ? "Dark Mode" : "Light Mode";
}

window.onload = function() {
    const container = document.createElement("div");
    container.className = "theme-toggle-container";

    const label = document.createElement("span");
    label.id = "theme-label";
    label.className = "theme-toggle-label";
    label.innerText = "Light Mode";

    const switchWrap = document.createElement("label");
    switchWrap.className = "theme-toggle-switch";

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.onchange = toggleTheme;

    const slider = document.createElement("span");
    slider.className = "slider";

    switchWrap.appendChild(checkbox);
    switchWrap.appendChild(slider);
    label.appendChild(switchWrap);
    container.appendChild(label);
    document.body.appendChild(container);
};