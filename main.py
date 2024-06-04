from network import LoRa
import socket
import time
import ubinascii
from pycoproc_1 import Pycoproc
from L76GNSS import L76GNSS
import pycom
import math

# Inicialización LoRa en LORAWAN mode.
# Europa = LoRa.EU868
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

# creación de los parámetros de autenticación OTAA

app_eui = ubinascii.unhexlify('70B3D549A759B792') ## app key
app_key = ubinascii.unhexlify('52FB223D34E4E71E9B4503E3648B76E5')


# conexión a la red utilizando OTAA (Over the Air Activation)
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

while not lora.has_joined():
    print('Not yet joined...')
    time.sleep(3)
#encendido del led para afirmar que la conexión ha sido un éxito
print("Joined network")
pycom.heartbeat(False)
pycom.rgbled(0x050005)
# creación del socket utilizado en la comunicación LoRa 
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
# configuración de la velocidad de datos
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

# Configurar Pytrack para obtener datos de GPS
py = Pycoproc(Pycoproc.PYTRACK)
l76 = L76GNSS(py, timeout=30)
primera_coord= None
cont_vueltas= 0
cambio_det= 0

try:
    while True:

        if cambio_det==1:
            time.sleep(30)
        else:
            time.sleep(120)  

        
        s.setblocking(True)


    # Obtener coordenadas GPS
        coord = l76.coordinates()      
        mov_vehiculo = 0
        if  coord[0] is  None and coord[1] is  None:
            print("no se pudieron obtener las coordenadas gps")
        else:
            cont_vueltas= cont_vueltas + 1
            latitude = coord[0]
            longitude = coord[1]
            print("coordenadas GPS validas",coord)
            if cont_vueltas == 1:
                primera_coord= coord
            #calculo de las variables para el margen de error a la hora de determinar si el vehículo se ha desplazado
            radio = 15
            radio_terrestre = 6371000
            Long_grado_long= 2 * math.pi * radio_terrestre *  math.cos(math.radians(latitude)) / 360
            Long_grado_lat= 2 * math.pi * radio_terrestre / 360
            increment_long = radio / Long_grado_long
            increment_lat = radio / Long_grado_lat

            if (abs(primera_coord[0]-coord[0]) > increment_lat)  or (abs(primera_coord[1]-coord[1]) > increment_long) :  
                print("La ubicacion ha cambiado.")
                mov_vehiculo = 1
            else:
                print("La ubicacion no ha cambiado.")
                mov_vehiculo = 0

        # Formatear datos de ubicación
            location_data = "{0},{1}, {2}".format(latitude, longitude, mov_vehiculo)
            print(location_data)
            s.send(location_data.encode())

    
        s.setblocking(False)

    # obtención si los hay de los datos enviados por el downlink
        data = s.recv(64)
        print(data)
        if data:
            cambio_det=1
except KeyboardInterrupt:
    print("Deteniendo la ejecución del programa...")

finally:
    # Intentar desconectar la conexión LoRa y cerrar el socket.
    try:
        if lora.has_joined():
            lora.disconnect()
            print("Desconexión de LoRa exitosa")
        
        s.close()
        print("Socket cerrado correctamente")
    
    except Exception as e:
        print("Error al cerrar la conexión LoRa y el socket:", e)
