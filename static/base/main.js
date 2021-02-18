// base script
// menu
const showMenu = (toggleId, navId) => {
    const toggle = document.getElementById(toggleId);
    const nav = document.getElementById(navId);
    const main = document.getElementById("main_page");
    const header = document.getElementById("page_header");
    const footer = document.getElementById("page_footer");

    if (toggle && nav) {
        toggle.addEventListener("click", () => {
            nav.classList.toggle("open_menu");
            toggle.classList.toggle("bx-x");
            main.classList.toggle("hide");
            header.classList.toggle("hide");
            footer.classList.toggle("hide");
        });
    }
};

showMenu("toggle_menu", "menubar");
