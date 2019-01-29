import matplotlib
matplotlib.use('agg')
import os 
import sys, os.path
import numpy as np
from astropy.io import fits
from matplotlib import pyplot as plt
import matplotlib.mlab as mlab
import pylab
import glob
import gc



'''
cut signal to noise at 2 so only accept galaxies with 2 or higher S/N 
do histogram of vdisp in log - max vdsip is 350 hardcap 
'''

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

hdu = fits.open('/Users/zak/Documents/project/ebossgalaxys.fits') 
plate_in = hdu[1].data['PLATE']
mjd_in = hdu[1].data['MJD']
fiberid_in = hdu[1].data['FIBERID']
z_in = hdu[1].data['Z']
vdisp_in = hdu[1].data['VDISP']
SN_in = hdu[1].data['SN_MEDIAN_ALL']

index = np.where(np.logical_and(vdisp_in>0,vdisp_in<350))
vdisp = vdisp_in[index]
vdisp = np.log10(vdisp)
print(vdisp)
print(max(vdisp))


plt.hist(vdisp,bins=50)

plt.xlabel("vdisp")
plt.ylabel("Frequency")
plt.title("Histogram of vdisp for eBOSS")
plt.show()
plt.savefig('vdisphistogram.pdf')