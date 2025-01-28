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