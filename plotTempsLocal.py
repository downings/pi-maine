#!/usr/bin/env python
import urllib2
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
#import matplotlib
import numpy
import datetime

numDays2Plot = 7  # number of days to plot
dataTable4 = []
#f = open('temperatureLog.txt')  # testing on AIR
f = open('/var/www/temperatureLog.txt')
for line in f:
    d = line.split(",")     # change string to list of strings
    if len(d) == 4:
        dataTable4.append(d)  # inside, furnace room, outside temperatures

# find index for date numDays2Plot days prior
start_date = datetime.datetime.now() + datetime.timedelta(-numDays2Plot)
s=start_date.strftime("%Y-%m-%d %H:%M:%S")
sa = numpy.array(s)

dataArray = numpy.array(dataTable4)
indxD = 0
for date in dataArray[:,0]:
    if sa < date:
        break  # found first occurance
    indxD = indxD + 1

tempInside = dataArray[indxD:-1,1]  # second column of array
tempOutside = dataArray[indxD:-1,3]
tempFurnance = dataArray[indxD:-1,2]

# convert date-time strings to matplotlib internal floating point representation
dateArray = [matplotlib.dates.datestr2num(i) for i in dataArray[indxD:-1,0]]
dateToday = matplotlib.dates.datestr2num(s)

#plt.gca().xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%m/%d/%Y %H:%M'))
plt.gca().xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(matplotlib.dates.DayLocator())
plt.gca().xaxis.set_minor_locator(matplotlib.dates.HourLocator())

plt.plot(dateArray, tempInside, '.b')
plt.plot(dateArray, tempOutside, '.r')
plt.plot(dateArray, tempFurnance, '.g')

plt.gcf().autofmt_xdate()
plt.ylabel('Degrees (F)')
plt.title('Temperatures')
legend = plt.legend(['inside', 'outside', 'radiator'], loc=(2), ncol=3, numpoints=1, frameon='None')
frame = legend.get_frame()
frame.set_facecolor('0.85')
frame.set_alpha(0.2)
frame.set_linewidth(0)

plt.grid(color='k', axis='y', linestyle='--', linewidth=0.5)
plt.grid(color='k', axis='x', linestyle=':', linewidth=0.5)

#plt.savefig('2temps.png', bbox_inches='tight')  # testing on AIR
#plt.savefig('2temps.png')  # testing on AIR
plt.savefig('/var/www/2temps.png', bbox_inches='tight')
#plt.show()

