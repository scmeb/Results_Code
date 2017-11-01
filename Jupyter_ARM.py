
from netCDF4 import Dataset
import os
import numpy as np
import matplotlib
from pylab import *
import time

import Calculating_variables as cv


import matplotlib.pyplot as plt


for root, dirs, files in os.walk(r'/home/cserv1_a/soc_pg/scmeb/Documents/Moist_Convection/Soundings/ARM_Data/Radioscondes_Jun_Sep'):
    for file in files:
        if file.endswith('.nc'):
            filename.append(''.join(['/home/cserv1_a/soc_pg/scmeb/Documents/Moist_Convection/Soundings/ARM_Data/Radioscondes_Jun_Sep',file]))


#nc_file = Dataset('/home/cserv1_a/soc_pg/scmeb/Documents/Moist_Convection/Soundings/ARM_Data/nimmergesonde1maceM1.c1.20060802.000000.cdf','r', format = 'NETCDF3_CLASSIC')
nc_file = Dataset('/home/cserv1_a/soc_pg/scmeb/Documents/Moist_Convection/Soundings/ARM_Data/Radioscondes_Jun_Sep/nimsondewnpnM1.b1.20060107.161400.cdf','r', format = 'NETCDF3_CLASSIC')
print(nc_file.variables)

# Load the different variables
pot_temp = nc_file.variables['alt']
time_obj = nc_file.variables['time']

# Load base_time (epoch time) and time_offset
bt_obj = nc_file.variables['base_time']
to_obj = nc_file.variables['time_offset']

# Load the time and temperature data into the workspace
base_time = bt_obj[:]
time_offset = to_obj[:]
pot_val = pot_temp[:]
time_org = time_obj[:]

print(pot_val)

t0 = base_time + time_offset[:]
time_hour = time_org/3600

# Next convert this time from epoch to the above structure
ts = []
for x in t0:
	current_t = time.gmtime(x)
	current_hour = current_t[3] + (current_t[4]/60)
	ts = ts + [current_hour]
print(shape(ts))

# Print date and time by converting the appropriate structure elements to strings
str_date = 'The date is: ' + repr(ts[1]) + '/' + repr(ts[2]) + '/' + repr(ts[0])
#print(str_date)
str_time = 'and the time (GMT) is: ' + repr(ts[3]) + ':' + repr(ts[4]) + ':' + repr(ts[5])

plot(ts,pot_val)
savefig('juptestplot.png',format='png')
plt.show


