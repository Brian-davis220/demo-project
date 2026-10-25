// main.js
// Handles delete confirmation and optional UI enhancements.

document.addEventListener('DOMContentLoaded', function () {
    // Confirm before deleting a link
    const deleteButtons = document.querySelectorAll('.delete-btn');
    deleteButtons.forEach(function (btn) {
        btn.addEventListener('click', function (e) {
            const title = btn.getAttribute('data-link-title') || 'this link';
            if (!confirm(`Are you sure you want to delete "${title}"?`)) {
                e.preventDefault();
            }
        });
    });

    // Dismiss messages on click
    const messages = document.querySelectorAll('.message');
    messages.forEach(function (msg) {
        msg.addEventListener('click', function () {
            msg.remove();
        });
    });
});
