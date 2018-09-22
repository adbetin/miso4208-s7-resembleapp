$(function () {
    $("#execute").click(function (e) {
        $( "#execute" ).prop( "disabled", true );

        e.preventDefault();
        $.ajax({
            type: "POST",
            url: process_url,
            data: {csrfmiddlewaretoken: csrf_token},
            success: function (data) {
                console.log("Ejecutado correctamente", data);
                alert("Ejecutado correctamente");
                location. reload(true);
            },
            error: function (error) {
                alert("Error al procesar");
            }
        });
    });
});
