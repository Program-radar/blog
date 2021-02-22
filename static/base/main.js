// base script
// menu
const showMenu = (toggleId, navId) => {
    const toggle = document.getElementById(toggleId);
    const nav = document.getElementById(navId);

    if (toggle && nav) {
        toggle.addEventListener("click", () => {
            nav.classList.toggle("open_menu");
            toggle.classList.toggle("bx-x");
        });
    }
};

showMenu("toggle_menu", "menubar");