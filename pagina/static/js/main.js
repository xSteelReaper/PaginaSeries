document.addEventListener('DOMContentLoaded', () => {
    const elementosCarousel = document.querySelectorAll('.carousel');
    M.Carousel.init(elementosCarousel, {
        duration: 0.5,
        dist: -70,
        shift: 5,
        padding: 5,
        numVisible: 5,
        indicators: true,
        noWrap: false
    });
});



$(document).ready(function() {
    $("#basic-form").validate({
        rules: {
            nick: {
                required: true,
                minlength: 3
            },
            email: {
                required: true,
                email: true
            },
            contraseña: {
                required: true,

            },
            contraseñar: {
                required: true,

            }
        }
    });
});



//validaciones
var emailPattern = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,4}$";

function checkInput(idInput, pattern) {
    return $(idInput).val().match(pattern) ? true : false;
}

function checkLongInput(idInput) {
    return $(idInput).val().length >= 5 ? true : false;
}

function enableSubmit(idForm) {
    $(idForm + " input.submit").removeAttr("disabled");
}

function disableSubmit(idForm) {
    $(idForm + " input.submit").attr("disabled", "disabled");
}

function checkLogin(idForm) {
    $(idForm + " *").on("change keydown", function() {
        if (checkInput("#loginEmail", emailPattern) &&
            checkLongInput("#loginPassword")) {
            enableSubmit(idForm);
        } else {
            disableSubmit(idForm);
        }
    });
}