import os 
import sys, os.path
import numpy as np
from astropy.io import fits
from matplotlib import pyplot as plt
import matplotlib.mlab as mlab
import pylab
import glob
import gc


directory = '/users/zak/Documents/output/FireFly_eBOSS/z_0.7_0.8/CB_D_C2'

allfits = glob.glob(directory+'/*.fits')
#initial arrays
chi_arr_1 = []
Z_1 = []
logAge_1 = []
vdisp = [1.95,2.05,2.15,2.25,2.35,2.45]
for filename in allfits:
	hdu = fits.open(filename)
	metallicity = hdu[1].header['metallicity_lightW'] #Z/H
	age = hdu[1].header['age_lightW'] #log(age/Gyr)
	print(filename)

	Z_1.append(metallicity)
	logAge_1.append(age)

	data = hdu[1].data['original_data']
	model = hdu[1].data['firefly_model']
	chi = np.mean(abs((data - model)/data)) 
	chi_arr_1.append(chi) #calculating the chi value (seeing how good the fit is)



directory = '/users/zak/Documents/output/FireFly_eBOSS/z_0.7_0.8/CB_C2_SLAQ'

allfits = glob.glob(directory+'/*.fits')
#initial arrays
chi_arr_2 = []
Z_2 = []
logAge_2 = []
for filename in allfits:
	hdu = fits.open(filename)
	metallicity = hdu[1].header['metallicity_lightW'] #Z/H
	age = hdu[1].header['age_lightW'] #log(age/Gyr)
	print(filename)

	Z_2.append(metallicity)
	logAge_2.append(age)

	data = hdu[1].data['original_data']
	model = hdu[1].data['firefly_model']
	chi = np.mean(abs((data - model)/data))
	chi_arr_2.append(chi) 

directory = '/users/zak/Documents/output/FireFly_eBOSS/z_0.7_0.8/CB_SLAQ_C3'

allfits = glob.glob(directory+'/*.fits')
#initial arrays
chi_arr_3 = []
Z_3 = []
logAge_3 = []
for filename in allfits:
	hdu = fits.open(filename)
	metallicity = hdu[1].header['metallicity_lightW'] #Z/H
	age = hdu[1].header['age_lightW'] #log(age/Gyr)
	print(filename)

	Z_3.append(metallicity)
	logAge_3.append(age)

	data = hdu[1].data['original_data']
	model = hdu[1].data['firefly_model']
	chi = np.mean(abs((data - model)/data))
	chi_arr_3.append(chi) 

directory = '/users/zak/Documents/output/FireFly_eBOSS/z_0.7_0.8/CB_C3_LRG'

allfits = glob.glob(directory+'/*.fits')
#initial arrays
chi_arr_4 = []
Z_4 = []
logAge_4 = []
for filename in allfits:
	hdu = fits.open(filename)
	metallicity = hdu[1].header['metallicity_lightW'] #Z/H
	age = hdu[1].header['age_lightW'] #log(age/Gyr)
	print(filename)

	Z_4.append(metallicity)
	logAge_4.append(age)

	data = hdu[1].data['original_data']
	model = hdu[1].data['firefly_model']
	chi = np.mean(abs((data - model)/data))
	chi_arr_4.append(chi) 


directory = '/users/zak/Documents/output/FireFly_eBOSS/z_0.7_0.8/CB_LRG_C5'

allfits = glob.glob(directory+'/*.fits')
#initial arrays
chi_arr_5 = []
Z_5 = []
logAge_5 = []
for filename in allfits:
	hdu = fits.open(filename)
	metallicity = hdu[1].header['metallicity_lightW'] #Z/H
	age = hdu[1].header['age_lightW'] #log(age/Gyr)
	print(filename)

	Z_5.append(metallicity)
	logAge_5.append(age)

	data = hdu[1].data['original_data']
	model = hdu[1].data['firefly_model']
	chi = np.mean(abs((data - model)/data))
	chi_arr_5.append(chi)


directory = '/users/zak/Documents/output/FireFly_eBOSS/z_0.7_0.8/CB_C5_C6'

allfits = glob.glob(directory+'/*.fits')
#initial arrays
chi_arr_6 = []
Z_6 = []
logAge_6 = []
for filename in allfits:
	hdu = fits.open(filename)
	metallicity = hdu[1].header['metallicity_lightW'] #Z/H
	age = hdu[1].header['age_lightW'] #log(age/Gyr)
	print(filename)

	Z_6.append(metallicity)
	logAge_6.append(age)

	data = hdu[1].data['original_data']
	model = hdu[1].data['firefly_model']
	chi = np.mean(abs((data - model)/data))
	chi_arr_6.append(chi)

directory = '/users/zak/Documents/output/FireFly_eBOSS/z_0.7_0.8/CB_C6_D'

allfits = glob.glob(directory+'/*.fits')
#initial arrays
chi_arr_7 = []
Z_7 = []
logAge_7 = []
for filename in allfits:
	hdu = fits.open(filename)
	metallicity = hdu[1].header['metallicity_lightW'] #Z/H
	age = hdu[1].header['age_lightW'] #log(age/Gyr)
	print(filename)

	Z_7.append(metallicity)
	logAge_7.append(age)

	data = hdu[1].data['original_data']
	model = hdu[1].data['firefly_model']
	chi = np.mean(abs((data - model)/data))
	chi_arr_7.append(chi)

vdisp2=[2.15,2.25,2.35,2.45] #needed as not all have bins have arrays for all vdisp

plt.plot(vdisp,Z_1,c='navy',label='D-C2')
plt.plot(vdisp,Z_2,c='skyblue',label='C2-2SLAQ')
plt.plot(vdisp,Z_3,c='seagreen',label='2SLAQ-C3')
plt.plot(vdisp,Z_4,c='olive',label='C3-LRG')
plt.plot(vdisp,Z_5,c='gold',label='LRG-C5')
plt.plot(vdisp,Z_6,c='orange',label='C5-C6')
plt.plot(vdisp2,Z_7,c='red',label='C6-D')

plt.ylim(-1.6,0.2)
plt.ylabel('Metallicity [Z/H]')
plt.xlabel('log(vdips/kms^-1)')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.title('0.7<z<0.8')
plt.show()