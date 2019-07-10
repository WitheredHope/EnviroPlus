from flask import Flask
import time
import ltr559
from enviroplus import gas
from bme280 import BME280
from subprocess import PIPE, Popen

try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)

def getGas():
    readings = gas.read_all()
    return(readings)

def getCpuTemp():
    process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE)
    output, _error = process.communicate()
    output = output.decode()
    return float(output[output.index('=') + 1:output.rindex("'")])

def getTemp():
    #adjust factor for better results, higher factor to increse temp
    factor = 0.8
    rawTemp = bme280.get_temperature()
    cpuTemp = getCpuTemp()
    calcTemp = rawTemp - (rawTemp-cpuTemp)/factor
    return(calcTemp)

def getPressure():
    return(bme280.get_pressure())

def getHumidity():
    return(bme280.get_humidity())

def getLight():
    return(ltr559.get_lux())


app = Flask(__name__)

@app.route("/")
def main():
    temp = getTemp()
    gas = getGas()
    pressure = getPressure()
    light = getLight()
    humidity = getHumidity()
    return ("""
            <meta http-equiv='refresh' content='1'>
            Welcome to the EnviroPi Webserver!<br/>
            Temperature = {} <br/>
            Gas = {} <br/>
            Pressure = {} <br/>
            Light = {} <br/>
            Humidity = {} <br/>
        """.format(temp, gas, pressure, light, humidity))
@app.route("/debug")
def debug():
    cpuTemp = getCpuTemp()
    rawTemp = bme280.get_temperature()
    temp = getTemp()
    return("""
    CPU Temp = {} <br/>
    Raw Temp = {} <br/>
    Temp = {} <br/>
    """.format(cpuTemp, rawTemp, temp))