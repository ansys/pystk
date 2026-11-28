// Force download for .ipynb links instead of rendering them in the browser.
document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll('a[href$=".ipynb"]').forEach(function (link) {
        link.setAttribute("download", "");
    });
});
