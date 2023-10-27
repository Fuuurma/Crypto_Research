document.addEventListener('DOMContentLoaded', function () {
    const app = document.getElementById('app');
    const modeToggle = document.getElementById('mode-toggle');
    const navbar = document.querySelector('.navbar');
    const savedMode = localStorage.getItem('mode');

    function setMode(mode) {
        app.classList.remove('light-mode', 'dark-mode');
        navbar.classList.remove('light-mode', 'dark-mode');
        app.classList.add(mode);
        navbar.classList.add(mode);
        localStorage.setItem('mode', mode);
    }

    modeToggle.addEventListener('click', function () {
        if (app.classList.contains('light-mode')) {
            setMode('dark-mode');
        } else {
            setMode('light-mode');
        }
    });

    if (savedMode) {
        setMode(savedMode);
    }
});


$(document).ready(function() {
    // Initial state: Show the general table and hide the favorite table
    $('#coins-general-container').show();
    $('#coins-favs-container').hide();

    // Handle button click
    $('#toggle-table-button').on('click', function() {
        // Toggle the visibility of the general and favorite tables
        $('#coins-general-container').toggle();
        $('#coins-favs-container').toggle();
    });
});

