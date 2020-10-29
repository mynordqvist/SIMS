import Adafruit_DHT
import qwiic_ccs811
import time
import globals

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

#Read the co2 value and update global variable
def Co2Variable():
    ccs = qwiic_ccs811.QwiicCcs811()
    ccs.begin()
    while True:
        ccs.read_algorithm_results() #updates the TVOC and CO2 values
        tvoc = ccs.get_tvoc()
        co2 = ccs.get_co2()
        time.sleep(5)
        globals.co2 = co2

#Return specific phrase depending on co2 value
def Co2():

    co2 = globals.co2
    
    if co2 < 600:
        return "Väldigt bra"
    
    elif co2 <800 and co2 >=600:
        return "Bra"
    
    elif co2 <1000 and co2 >=800:
        return "Ganska dålig, vädra gärna"
        
    
    elif co2 <2000 and co2 >=1000:
        return "Dålig, ni måste vädra! Annars kan trötthet och huvudvärk uppstå"
    
    elif co2 <=6000 and co2 >=2000:
        return "Väldigt dålig, detta är maximala gränsen enligt Arbetsmiljöverket. Nu måste ni vädra!"
        
    
    elif co2 > 6000:
        return "Extremt dålig, ni får inte vistas i denna luft längre än 15 minuter!"  
