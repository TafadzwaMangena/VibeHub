/**
 * Displaying django message.
 */
document.addEventListener("DOMContentLoaded", function () {
    const djangoMessage = document.getElementById("django-message");

    if (djangoMessage) {
        // Make the message visible
        djangoMessage.style.display = "block";

        // Automatically fade out the message after 10 seconds
        setTimeout(() => {
            djangoMessage.style.opacity = "0"; // Gradually fade out
            setTimeout(() => djangoMessage.style.display = "none", 1000); // Hide it completely after fading
        }, 10000);
    }
});

/**
 * Enable Bootstrap tooltips for disabled report button.
 */
document.addEventListener("DOMContentLoaded", function () {
    // Select all elements with the tooltip attribute
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));

    // Initialize Bootstrap tooltips for each element found
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
});
