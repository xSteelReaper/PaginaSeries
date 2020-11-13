$(function() {
    $('#login').click(function() {
        $(this).next('#login-content').slideToggle();
        $(this).toggleClass('active');
    });
});

document.addEventListener('DOMContentLoaded', function() {
    M.AutoInit();
});