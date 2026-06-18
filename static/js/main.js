document.querySelectorAll(".form-range").forEach((range) => {
    const label = range.previousElementSibling;
    const updateLabel = () => {
        label.textContent = label.textContent.replace(/\s\(\d+\)$/, "") + ` (${range.value})`;
    };

    range.addEventListener("input", updateLabel);
    updateLabel();
});

const themeToggle = document.querySelector(".theme-toggle");

if (themeToggle) {
    const themeIcon = themeToggle.querySelector(".theme-toggle-icon");
    const themeText = themeToggle.querySelector(".theme-toggle-text");

    const updateThemeButton = () => {
        const isDark = document.documentElement.dataset.theme === "dark";
        themeIcon.textContent = isDark ? "☀" : "☾";
        themeText.textContent = isDark ? "Light" : "Dark";
        themeToggle.setAttribute("aria-label", isDark ? "Switch to light mode" : "Switch to dark mode");
    };

    themeToggle.addEventListener("click", () => {
        const nextTheme = document.documentElement.dataset.theme === "dark" ? "light" : "dark";
        document.documentElement.dataset.theme = nextTheme;
        localStorage.setItem("theme", nextTheme);
        updateThemeButton();
    });

    updateThemeButton();
}
