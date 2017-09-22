# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 17:04:32 2017

@author: eebjw
"""

from __future__ import division
import numpy as np

def compute_theta_e(temp,p,r):

	# Calculates equivalent potential temperature, which is the temperature an 
    	# air mass would have if expanded adiabatically to 1000 hPa and all water vapor is condensed.
	# Formula taken from Stull 1988 13.1 p. 546
	# INPUTS:
	# temp: Temperature, K.
	# p: Pressure, hPa
	# r: water vapor mixing ratio, kg h2o per kg dry air (or can use specific humidity)	

    Rd = 287.04 #specific gas constant for air, J/kg/K
    Lv = 2.25e6 #latent heat of vaporization, J/kg
    cpd = 1004 #heat capacity of dry air at constant p, J/K/kg
    p0 = 1000 #reference pressure, hPa

    
    theta_e = (temp + (Lv/cpd)*r)*(p0/p)**(Rd/cpd)
    return theta_e

def compute_theta (temp,p,**kwargs):
    
	# Calculates potential temperature, which is the temperature an air mass would acquire if adiabatically brought to 1000 hPa.
	# Formula taken from Stull 1988 13.1 p. 546
	# INPUTS:
	# temp: Temperature, K.
	# p: Pressure, hPa	
    
    Rd = 287.04 #specific gas constant for air, J/kg/K
    cpd = 1004 #heat capacity of dry air at constant p, J/K/kg
    p0 = 1000 #reference pressure, hPa
    
    
    theta = temp*(p0/p)**(Rd/cpd)
    return theta

def compute_temp (theta,p,**kwargs):
    
	# Calculates temperature, 
	# Formula taken from Stull 1988 13.1 p. 546
	# INPUTS:
	# temp: Temperature, K.
	# p: Pressure, hPa	
    
    Rd = 287.04 #specific gas constant for air, J/kg/K
    cpd = 1004 #heat capacity of dry air at constant p, J/K/kg
    p0 = 1000 #reference pressure, hPa
    
    
    temp = theta*(p0/p)**(-Rd/cpd)
    return temp
