## TFG_ALBERTO_SANCHEZ_GIL
Este proyecto esta basado en la monitorización de la localización obtenida por un dispositivo final compuesto por una placa Pytrack y una LoPy4 usando la tecnología LoRaWAN. 
Como se explica en la plantilla [TFG_ALBERTO_SANCHEZ_GIL](https://github.com/AlbertoSanchezGil1/TFG_ALBERTO_SANCHEZ_GIL "TFG_ALBERTO_SANCHEZ_GIL")
## Instalación
Para poder instalar el archivo solo se necesitará tener un servidor de red, un servidor de aplicación y una plataforma IoT.
## Uso
Para utilizar el proyecto de manera local será necesario tener instalado:
- Github Desktop
- VSCode
- The Things Network
- DATACAKE
## Finalidad
Este trabajo será útil para aquellas personas que necesiten recordar la localización de su vehículo y la tranquilidad que genera saber en cada momento que el automóvil se encuentra en su ubicación y en caso de que no sea así tener una rápida capacidad de respuesta para arreglar la situación.
## Pymakr.conf
Este archivo contiene elementos de configuración como el nombre del proyecto y archivos y directorios que deben ser descartados a la hora de realizar determinadas funciones con un script de python.
## PyTrack-Geocode-workspace
Es un archivo de configuración que Visual Studio Code crea de manera automática, donde nos indica el directorio actual donde se encuentra la carpeta y el nombre del elemento externo detectado.
## Pycoproc_1.py y L76GNSS.py
Estos dos archivos de script Python son utilizados como librerías  para poder crear un objeto Pytrack y a partir de él poder utilizar el sensor de localización que posee para en el archivo principal “main.py” poder obtener la localización del automóvil. Han sido reutilizados del código expuesto en:
+ [Librería L76GNSS ](https://github.com/pycom/pycom-libraries/blob/master/shields/lib/L76GNSS.py)
+ [Librería pycoproc_1 ](https://github.com/pycom/pycom-libraries/blob/master/shields/lib/pycoproc_1.py )
## Main.py
Es el script principal del proyecto por el cual se va a producir la conexión a TTN y el envió de los datos necesarios  para realizar todas las funciones.
Hay que recalcar que  el código para establecer la conexión LoRaWAN entre el nodo y el servidor de red se ha obtenido de  
 https://github.com/pycom/pycom-libraries/blob/master/examples/OTA/1.0.1/flash/main.py
