// document.addEventListener('DOMContentLoaded', function () {
//     const app = document.getElementById('app');
//     const modeToggle = document.getElementById('mode-toggle');
//     const navbar = document.querySelector('.navbar');
//     const savedMode = localStorage.getItem('mode');

//     function setMode(mode) {
//         app.classList.remove('light-mode', 'dark-mode');
//         navbar.classList.remove('light-mode', 'dark-mode');
//         app.classList.add(mode);
//         navbar.classList.add(mode);
//         localStorage.setItem('mode', mode);
//     }

//     modeToggle.addEventListener('click', function () {
//         if (app.classList.contains('light-mode')) {
//             setMode('dark-mode');
//         } else {
//             setMode('light-mode');
//         }
//     });

//     if (savedMode) {
//         setMode(savedMode);
//     }
// });


// $(document).ready(function() {
//     // Initial state: Show the general table and hide the favorite table
//     $('#coins-general-container').show();
//     $('#coins-favs-container').hide();

//     // Handle button click
//     $('#toggle-table-button').on('click', function() {
//         // Toggle the visibility of the general and favorite tables
//         $('#coins-general-container').toggle();
//         $('#coins-favs-container').toggle();
//     });
// });



// Formatting Number functions

$(document).ready(function()
{
    format_all_numbers();
})




function format_all_numbers()
{
    const numbers = document.querySelectorAll('.number');
    const pct_changes = document.querySelectorAll('.pct-change');

    numbers.forEach((element) => {
        const value = parseFloat(element.textContent);

        if (!isNaN(value))
        {
            const changed_value = format_number(value);
            element.textContent = changed_value;
        }
        
        else
        {
            const changed_value = "-";
            // element.textContent = changed_value;
        }
    });

    pct_changes.forEach((element) => {
        const value = parseFloat(element.textContent);

        if (!isNaN(value))
        {
            if (value > 0)
            {
                element.classList.add('text-success');
            }
            else if (value < 0)
            {
                element.classList.add('text-danger');
            }
            else if (value == 0)
            {
                element.classList.add('text-dark');
            }
            
            const changed_value = format_pct_change(value);
            element.textContent = changed_value;
        }
        
    }
    )
}


function format_number(number)
{
    if (isNaN(number))
    {
        return '-';
    }
    
    if (Math.abs(number) >= 1e12) {
        return '$' + (number / 1e12).toFixed(2) + 'T';
      } else if (Math.abs(number) >= 1e9) {
        return '$' + (number / 1e9).toFixed(2) + 'B';
      } else if (Math.abs(number) >= 1e6) {
        return '$' + (number / 1e6).toFixed(2) + 'M';
      } else if (Math.abs(number) >= 1e3) {
        return '$' + (number / 1e3).toFixed(2) + 'K';
      } else {
        return '$' + number.toFixed(2);
      }
}


function format_pct_change(number)
{
    return number.toFixed(2) + '%';
}




//  Login & Register Functions to Show Password

$(document).ready(function()
{
    $('#showPassword').click(function() {
        const passwordInput = $('#password');
        const passwordFieldType = passwordInput.attr('type');
        const showPasswordIcon = $('#showPassword');

        if (passwordFieldType === 'password') {
            passwordInput.attr('type', 'text');
            showPasswordIcon.removeClass('bi bi-eye-slash').addClass('bi bi-eye');

        } else {
            passwordInput.attr('type', 'password');
            showPasswordIcon.removeClass('bi bi-eye').addClass('bi bi-eye-slash');
        }
    });
});


// For Protocols
document.addEventListener('DOMContentLoaded', function() {
    var rows = document.querySelectorAll('.protocol-row');
    rows.forEach(function(row) {
        row.addEventListener('click', function() {
            var protocolId = row.getAttribute('data-protocol-id');
            var url = 'protocols/' + protocolId;
            window.location.href = url;
        });
    });
});

// For Chains
document.addEventListener('DOMContentLoaded', function() {
    var rows = document.querySelectorAll('.chain-row');
    rows.forEach(function(row) {
        row.addEventListener('click', function() {
            var chain = row.getAttribute('data-protocol-id');
            var url = 'chains/' + chain;
            window.location.href = url;
        });
    });
});



// For fees link
$(document).ready(function () {
    $('.fee-link').on('click', function (event) {
        event.preventDefault();
        var name = $(this).data('name');
        window.location.href = '/fees/' + name;
    });
});