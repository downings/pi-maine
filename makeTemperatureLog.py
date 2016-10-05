#!/usr/bin/env python
# use crontab as:
# */15 * * * * /var/www/makeTemperatureLog.py &>/dev/null

import time
import urllib

timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

# get Pi temperature                                                                                                                                                                                        
tfile = open("/sys/bus/w1/devices/28-000006787fad/w1_slave")
text = tfile.read()
tfile.close()
temperature_data = text.split()[-1]
temperature = float(temperature_data[2:])
temperature = temperature / 1000
temperature = temperature * 9 / 5 + 32

# get furnance room temperature
#28-000006776dee
tfile = open("/sys/bus/w1/devices/28-000006776dee/w1_slave")
#tfile = open("/sys/bus/w1/devices/28-000006787fad/w1_slave")
text = tfile.read()
tfile.close()
temperature_data = text.split()[-1]
temperatureFR = float(temperature_data[2:])
temperatureFR = temperatureFR / 1000
temperatureFR = temperatureFR * 9 / 5 + 32

# get Outside temperature
site = "http://forecast.weather.gov/MapClick.php?lat=43.3256388100005&lon=-70.5\
5338889299964&site=all&smap=1#.VHFaX76lmRc"

response = urllib.urlopen(site)
html = response.read()
endOfTemp = html.find("&deg;F")
ch = html[endOfTemp]
index = endOfTemp
while ch != ">":
    index = index - 1
    ch = html[index]

startOfTemp = index + 1
textTemp = html[startOfTemp:endOfTemp]
tempInt = int(textTemp)

# append time, temperature to datafile                                                                                                                                                                          
#f = open('temperatureLog.txt', 'a')
f = open('/var/www/temperatureLog.txt', 'a')
#f.write(timestamp + ',' + str(temperature) + '\n')
#f.write(timestamp + ',' + str(temperature) + ',' + textTemp + '\n')
f.write(timestamp + ',' + str(temperature) + ',' + str(temperatureFR) + ',' + textTemp + '\n')
f.close()

