var servicioSelect;  // Declarar la variable globalmente

document.addEventListener('DOMContentLoaded', function () {
    servicioSelect = document.getElementById('servicio');
    var opcionesDiv = document.getElementById('opciones');
    var opcionesEstrategiasDiv = document.getElementById('opcionesEstrategias');
    var opcionesAudiovisualDiv = document.getElementById('opcionesAudiovisual');
    var opciones360Div = document.getElementById('opciones360');
    var opcionesBrandingDiv = document.getElementById('opcionesBranding');
    var opcionesConsultoraDiv = document.getElementById('opcionesConsultora');
    var opcionesLegalDiv = document.getElementById('opcionesLegal');
    var totalSpan = document.getElementById('total');

    servicioSelect.addEventListener('change', function () {
        resetOpciones();
        if (servicioSelect.value !== '0') {
            opcionesDiv.style.display = 'block';
            if (servicioSelect.value === 'estrategias') {
                opcionesEstrategiasDiv.style.display = 'block';
            } else if (servicioSelect.value === 'audiovisual') {
                opcionesAudiovisualDiv.style.display = 'block';
            } else if (servicioSelect.value === '360') {
                opciones360Div.style.display = 'block';
            } else if (servicioSelect.value === 'branding') {
                opcionesBrandingDiv.style.display = 'block';
            } else if (servicioSelect.value === 'consultora') {
                opcionesConsultoraDiv.style.display = 'block';
            } else if (servicioSelect.value === 'legal') {
                opcionesLegalDiv.style.display = 'block';
            }
        } else {
            opcionesDiv.style.display = 'none';
        }
        calcularTotal();
    });

    document.querySelectorAll('input[name="opcion"]').forEach(function (checkbox) {
        checkbox.addEventListener('change', calcularTotal);
    });

    function resetOpciones() {
        opcionesEstrategiasDiv.style.display = 'none';
        opcionesAudiovisualDiv.style.display = 'none';
        opciones360Div.style.display = 'none';
        opcionesBrandingDiv.style.display = 'none';
        opcionesConsultoraDiv.style.display = 'none';
        opcionesLegalDiv.style.display = 'none';
        document.querySelectorAll('input[name="opcion"]').forEach(function (checkbox) {
            checkbox.checked = false;
        });
    }
    function calcularTotal() {
        var total = parseInt(servicioSelect.value) || 0;
        document.querySelectorAll('input[name="opcion"]:checked').forEach(function (checkbox) {
            total += parseInt(checkbox.dataset.valor);
        });
    
        // Utiliza la función toLocaleString para formatear el número con separadores de miles
        totalSpan.textContent = '$' + total.toLocaleString('es-CL');
    }
    
    document.getElementById('cotizacionForm').addEventListener('submit', function (e) {
        e.preventDefault();
        calcularTotal();
        alert('Cotización generada. Total: ' + totalSpan.textContent);
    });
    
});
