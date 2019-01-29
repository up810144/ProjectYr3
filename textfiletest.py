import os 
import sys, os.path
import numpy as np
from astropy.io import fits
from matplotlib import pyplot as plt
import matplotlib.mlab as mlab
import pylab
import glob
import gc





#constants for stacking 
minlam = 3.4771
maxlam = 3.7446

step_size = 0.0001
array_length = int((maxlam-minlam)/step_size)

flux_array = np.arange(minlam,maxlam,step_size)
print(np.shape(flux_array))

interp_array = np.arange(minlam,maxlam,step_size) #array of x co-ordinates for interp values (common wavelength grid)

var_array = np.arange(minlam,maxlam,step_size) 
error_array = np.arange(minlam,maxlam,step_size)
number_stacked = 0

#bin creation

hdu = fits.open('/Users/zak/Documents/placement/eBOSS_data_table_firefly/ebossgalaxys.fits') 
plate_in = hdu[1].data['PLATE']
mjd_in = hdu[1].data['MJD']
fiberid_in = hdu[1].data['FIBERID']
z_in = hdu[1].data['Z']
vdisp_in = hdu[1].data['VDISP']
SN_in = hdu[1].data['SN_MEDIAN_ALL']

index = np.where(np.logical_and(z_in>0.3,z_in<0.4))
z = z_in[index]
vdisp = vdisp_in[index]
plate = plate_in[index]
mjd = mjd_in[index]
fiberid = fiberid_in[index]
index2 = np.where(np.logical_and(vdisp>230,vdisp<240))
vdisp = vdisp[index2]
z = z[index2]
plate = plate[index2]
mjd = mjd[index2]
fiberid =  fiberid[index2]
#plate = np.array2string(plate,separator=',')
plate = list(map(str,plate))

(type(plate))
print(plate)
print(mjd)
print(fiberid)
print(len(plate))



