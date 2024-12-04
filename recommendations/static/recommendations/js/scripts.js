// static/recommendations/js/scripts.js
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        const input = form.querySelector('input[name="movie_name"]');
        if (input.value === '') {
            event.preventDefault();
            alert('Please enter a movie name');
            input.style.border = '2px solid red';
        } else {
            input.style.border = '';
        }
    });
});
