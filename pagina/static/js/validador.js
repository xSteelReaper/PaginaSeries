$("#formulario1").validate({
    rules: {
        "txtEmail": {
            required: true,
            email: true
        },
        "txtRut": {
            required: true
        },
        "txtNombre": {
            required: true
        },
        "txtFecha": {
            required: true
        },
        "txtTelefono": {
            required: true
        },
        "cbRegion": {
            required: true
        },
        "cbCiudad": {
            required: true
        },
        "cbDomicilio": {
            required: true
        }
    },
    messages: {
        "txtEmail": {
            required: "Te falto el email",
            email: "No tiene formato email"
        },
        "txtRut": {
            required: "Te falto el run"
        },
        "txtNombre": {
            required: "Te falto el nombre"
        },
        "txtFecha": {
            required: "Te falto la fecha",
            max: "Año de nacimiento anterior a 2001"
        },
        "txtTelefono": {
            required: "Te falto el telefono"
        },
        "cbRegion": {
            required: "Te falto la region"
        },
        "cbCiudad": {
            required: "Te falto la ciudad"
        },
        "cbDomicilio": {
            required: "Te falto el domicilio"
        }
    }
}
);

function soloLetras(e) {
    key = e.keyCode || e.which;
    tecla = String.fromCharCode(key).toLowerCase();
    letras = " áéíóúabcdefghijklmnñopqrstuvwxyz";
    especiales = "8-37-39-46";

    tecla_especial = false
    for (var i in especiales) {
        if (key == especiales[i]) {
            tecla_especial = true;
            break;
        }
    }

    if (letras.indexOf(tecla) == -1 && !tecla_especial) {
        return false;
    }
}
