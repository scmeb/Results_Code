#!/bin/env python
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as N
import matplotlib.pyplot as plt
import matplotlib.animation 
import sys                   # interface with operating system and shell environment
import math as m
import iris as rs
import os  # os.path - try importing functions within folders maybe



import Calculating_variables as cv 
from netCDF4 import Dataset

filename = './../RKW_Test/Line_run_2500shear/Line_run_2500shear.nc'

dataset = Dataset(filename)

print(dataset.file_format)
print(dataset.dimensions.keys())
print(dataset.dimensions['ni'])
print(dataset.variables.keys())
print(dataset.variables['prs'])

# Create variables
X = dataset.variables['xh'][:]
Y = dataset.variables['yh'][:]
Z = dataset.variables['z'][:]
TH = dataset.variables['th'][:]
MIX = dataset.variables['qc'][:]
W = dataset.variables['w'][:]
TK = dataset.variables['tke'][:] 
PRS = dataset.variables['prs'][:] 


# Choose number of contour lines
def Levels(Var):
    min_var = Var.min()
    max_var = Var.max()
    
    no = (max_var - min_var)/3
    
    levels = N.linspace(min_var,max_var,no)
    
    return levels

# Create plot to compare to original RKW paper and Bryan
def VelocityandWatervapourGraph(filename):

    i = 1
    
    while i < 25: #25:
        

        levels = Levels(W[i,:,:,:])
        
        plt.contour(X[400:580], Y[0:80], MIX[i,6,0:80,400:580], colors = 'k')
        plt.contourf(X[400:580], Y[0:80], W[i,6,0:80,400:580], levels = levels)
       
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title(''.join([repr(dataset.variables['time'][i]/(60*60)), ' hours']) )
        plt.colorbar()
        #plt.savefig(''.join([filename,'_' ,repr(i),'_WandMix.png']))
        plt.show()
    	
        # Find equivalent potential temperature
        TEMP = cv.compute_temp(TH[i,:,:,:],PRS[i,:,:,:]/100)
        TH_E = cv.compute_theta_e(TEMP,PRS[i,:,:,:]/100,MIX[i,:,:,:])
        TH_E.shape
        
	
        plt.contourf(X[400:550], Z[0:10], TH_E[0:10,50,400:550])#, levels = levels)
        plt.xlabel('Y')
        plt.ylabel('Z')
        plt.title(''.join([repr(dataset.variables['time'][i]/(60*60)), ' hours']) )
        plt.colorbar()
        plt.savefig(''.join([filename,'_' ,repr(i),'_WandMix.png']))
        plt.show()
       
        i = i + 3
        """ 
        plt.contourf(X[400:550], Z[:], TH_E[:,50,400:550])#, levels = levels)
        plt.colorbar()
        plt.show()
        """
     
        
    plt.close('all')
    os.system('./make_video_from_image.sh')

    return TH_E

"""   
    i = 1
    while i < 20:
        plt.contour(X[300:600], Z[1:20], TH[i,1:20,98,300:600],10)
        plt.xlabel('X')
        plt.ylabel('Z')
        plt.title(dataset.variables['time'][i]/(60*60) )
        plt.show()
        i = i + 1
        
    
    i = 1
    while i < 25:
        plt.contour(Y, Z, U[i,:,:,120])
        plt.xlabel('Y')
        plt.ylabel('Z')
        plt.title(dataset.variables['time'][i]/(60*60) )
        plt.show()
        i = i + 1
"""



TH_E = VelocityandWatervapourGraph(filename)

     
dataset.close()
