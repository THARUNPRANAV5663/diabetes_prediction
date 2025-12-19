document.addEventListener("DOMContentLoaded", function () {
    const toggle = document.getElementById("themeToggle");
    const body = document.body;

    // Load saved theme
    if (localStorage.getItem("theme") === "light") {
        body.classList.add("light-theme");
        toggle.checked = true;
    }

    toggle.addEventListener("change", function () {
        if (toggle.checked) {
            body.classList.add("light-theme");
            localStorage.setItem("theme", "light");
        } else {
            body.classList.remove("light-theme");
            localStorage.setItem("theme", "dark");
        }
    });
});