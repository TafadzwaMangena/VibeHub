document.addEventListener("DOMContentLoaded", function () {
    const djangoMessage = document.getElementById("django-message");

    if (djangoMessage) {
        // Show the message
        djangoMessage.style.display = "block";
        
        // To fade out the message after 10 seconds
        setTimeout(() => {
            djangoMessage.style.opacity = "0";
            setTimeout(() => djangoMessage.style.display = "none", 1000);
        }, 10000);
    }
});

// Add tooltip functionality to elements with the "tooltip" data attribute
document.addEventListener("DOMContentLoaded", function () {
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
});
