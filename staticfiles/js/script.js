/**
 * Displaying django message.
 * Make the message visible,
 * Automatically fade out the message after 10 seconds,
 * Gradually fade out,
 * Hide it completely after fading.
 */
document.addEventListener("DOMContentLoaded", function () {
    const djangoMessage = document.getElementById("django-message");

    if (djangoMessage) {
        djangoMessage.style.display = "block";
        setTimeout(() => {
            djangoMessage.style.opacity = "0";
            setTimeout(() => djangoMessage.style.display = "none", 1000);
        }, 10000);
    }
});

/**
 * Enable Bootstrap tooltips for disabled report button.
 * Select all elements with the tooltip attribute,
 * Initialize Bootstrap tooltips for each element found.
 */
document.addEventListener("DOMContentLoaded", function () {
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
});
