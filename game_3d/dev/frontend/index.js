import { router } from "./helpers/router.js";
import { navigateTo } from "./helpers/navigateto.js";

// Global variables
export const openChatWebSockets = {};

window.apiUrl = 'https://localhost/api/';

export const sockets = {};

window.addEventListener("popstate", navigateTo(window.location.pathname));

document.addEventListener("DOMContentLoaded", () => {
    document.body.addEventListener("click", e => {
        if (e.target.matches("[data-link]")) {
            e.preventDefault();
			navigateTo(e.target.href);
        }
    });
    router();
});

function nonHtml(){
    return    this.replace(/[&<>"'`]/g, function (char){
        const map = {
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            '"': '&quot;',
            "'": '&apos;',
            '`': '&#96;'
        }
    });
}