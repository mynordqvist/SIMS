import Adafruit_DHT

#Read humidity and temperature values from sensor
def Read_sensor():
    sensor = Adafruit_DHT.DHT11
    gpio = 27

    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio) #Read from sensor
    
    return humidity, temperature

#Return the temperature in celsius
def Temperature():
    
    humidity, temperature = Read_sensor()
    
    return int(temperature)

#Return the humdity in percent
def Humidity():
    
    humidity, temperature = Read_sensor()
    
    return int(humidity)
    