#Librería para el sensor MQ2


import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn


#Esta función configura al sensor 
def configuracion_MQ2():
    #Creación del canal SPI
    spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

    #Selección del pin donde se conecta el CS del MCP3008 en la rasp
    cs = digitalio.DigitalInOut(board.D5) #D5=GPIO5

    #Creación del objeto MCP3008
    mcp = MCP.MCP3008(spi, cs)

    #Creación de una entrada analogica en el canal 0 del MCP3008
    chan = AnalogIn(mcp, MCP.P0)

    return chan


#Esta función retorna el valor de gas y humo detectado
def medicion_gas(chan):
    return chan.voltage