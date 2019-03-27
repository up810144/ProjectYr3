import os
import sys, os.path
import numpy as np
from astropy.io import fits
from matplotlib import pyplot as plt
import matplotlib.mlab as mlab
import pylab
import glob
import gc
from operator import add


directory = '/users/zak/Documents/output/FireFly_eBOSS/z_0.5_0.6/CB_D_C2'
allfits = glob.glob(directory+'/*.fits')
#initial arrays

vdisp = [1.95,2.05,2.15,2.25,2.35,2.45]
N=['1','2','3','4','5','6']
chi_arr_1 = []
Z_1 = []
logAge_1 = []
Z_1_up_err=[]
Z_1_low_err=[]
for i in range(6):
	filename = '/users/zak/Documents/output/FireFly_eBOSS/z_0.5_0.6/CB_D_C2/spFly-z0506_CBDC2_V'+N[i]+'_DAP.fits'
	hdu = fits.open(filename)
	metallicity = hdu[1].header['metallicity_lightW'] #Z/H
	age = hdu[1].header['age_lightW'] #log(age/Gyr)
	Z_1_up_error = hdu[1].header['metallicity_lightW_up_1sig'] - metallicity
	Z_1_low_error = metallicity - hdu[1].header['metallicity_lightW_low_1sig']
	Z_1_up_err.append(Z_1_up_error)
	Z_1_low_err.append(Z_1_low_error)


	Z_1.append(metallicity)
	logAge_1.append(age)


	data = hdu[1].data['original_data']
	model = hdu[1].data['firefly_model']
	chi = np.mean(abs((data - model)/data))
	chi_arr_1.append(chi)




#initial arrays
chi_arr_2 = []
Z_2 = []
logAge_2 = []
Z_2_up_err=[]
Z_2_low_err=[]
for i in range(6):
	filename = '/users/zak/Documents/output/FireFly_eBOSS/z_0.5_0.6/CB_C2_SLAQ/spFly-z0506_CBC2SLAQ_V'+N[i]+'_DAP.fits'
	hdu = fits.open(filename)
	metallicity = hdu[1].header['metallicity_lightW'] #Z/H
	age = hdu[1].header['age_lightW'] #log(age/Gyr)
	Z_2_up_error = hdu[1].header['metallicity_lightW_up_1sig'] - metallicity
	Z_2_low_error = metallicity - hdu[1].header['metallicity_lightW_low_1sig']
	Z_2_up_err.append(Z_2_up_error)
	Z_2_low_err.append(Z_2_low_error)

	Z_2.append(metallicity)
	logAge_2.append(age)

	data = hdu[1].data['original_data']
	model = hdu[1].data['firefly_model']
	chi = np.mean(abs((data - model)/data))
	chi_arr_2.append(chi)


#initial arrays
chi_arr_3 = []
Z_3 = []
logAge_3 = []
Z_3_up_err=[]
Z_3_low_err=[]
for i in range(6):
	filename = '/users/zak/Documents/output/FireFly_eBOSS/z_0.5_0.6/CB_SLAQ_C3/spFly-z0506_CBSLAQC3_V'+N[i]+'_DAP.fits'
	hdu = fits.open(filename)
	metallicity = hdu[1].header['metallicity_lightW'] #Z/H
	age = hdu[1].header['age_lightW'] #log(age/Gyr)
	Z_3_up_error = hdu[1].header['metallicity_lightW_up_1sig'] - metallicity
	Z_3_low_error = metallicity - hdu[1].header['metallicity_lightW_low_1sig']
	Z_3_up_err.append(Z_3_up_error)
	Z_3_low_err.append(Z_3_low_error)

	Z_3.append(metallicity)
	logAge_3.append(age)

	data = hdu[1].data['original_data']
	model = hdu[1].data['firefly_model']
	chi = np.mean(abs((data - model)/data))
	chi_arr_3.append(chi)


#initial arrays
chi_arr_4 = []
Z_4 = []
logAge_4 = []
Z_4_up_err=[]
Z_4_low_err=[]
for i in range(6):
	filename = '/users/zak/Documents/output/FireFly_eBOSS/z_0.5_0.6/CB_C3_LRG/spFly-z0506_CBC3LRG_V'+N[i]+'_DAP.fits'
	hdu = fits.open(filename)
	metallicity = hdu[1].header['metallicity_lightW'] #Z/H
	age = hdu[1].header['age_lightW'] #log(age/Gyr)
	Z_4_up_error = hdu[1].header['metallicity_lightW_up_1sig'] - metallicity
	Z_4_low_error = metallicity - hdu[1].header['metallicity_lightW_low_1sig']
	Z_4_up_err.append(Z_4_up_error)
	Z_4_low_err.append(Z_4_low_error)

	Z_4.append(metallicity)
	logAge_4.append(age)

	data = hdu[1].data['original_data']
	model = hdu[1].data['firefly_model']
	chi = np.mean(abs((data - model)/data))
	chi_arr_4.append(chi)



#initial arrays
chi_arr_5 = []
Z_5 = []
logAge_5 = []
Z_5_up_err=[]
Z_5_low_err=[]
for i in range(6):
	filename = '/users/zak/Documents/output/FireFly_eBOSS/z_0.5_0.6/CB_LRG_C5/spFly-z0506_CBLRGC5_V'+N[i]+'_DAP.fits'
	hdu = fits.open(filename)
	metallicity = hdu[1].header['metallicity_lightW'] #Z/H
	age = hdu[1].header['age_lightW'] #log(age/Gyr)
	Z_5_up_error = hdu[1].header['metallicity_lightW_up_1sig'] - metallicity
	Z_5_low_error = metallicity - hdu[1].header['metallicity_lightW_low_1sig']
	Z_5_up_err.append(Z_5_up_error)
	Z_5_low_err.append(Z_5_low_error)

	Z_5.append(metallicity)
	logAge_5.append(age)

	data = hdu[1].data['original_data']
	model = hdu[1].data['firefly_model']
	chi = np.mean(abs((data - model)/data))
	chi_arr_5.append(chi)



#initial arrays
chi_arr_6 = []
Z_6 = []
logAge_6 = []
Z_6_up_err=[]
Z_6_low_err=[]
for i in range(6):
	filename = '/users/zak/Documents/output/FireFly_eBOSS/z_0.5_0.6/CB_C5_C6/spFly-z0506_CBC5C6_V'+N[i]+'_DAP.fits'
	hdu = fits.open(filename)
	metallicity = hdu[1].header['metallicity_lightW'] #Z/H
	age = hdu[1].header['age_lightW'] #log(age/Gyr)
	Z_6_up_error = hdu[1].header['metallicity_lightW_up_1sig'] - metallicity
	Z_6_low_error = metallicity - hdu[1].header['metallicity_lightW_low_1sig']
	Z_6_up_err.append(Z_6_up_error)
	Z_6_low_err.append(Z_6_low_error)

	Z_6.append(metallicity)
	logAge_6.append(age)

	data = hdu[1].data['original_data']
	model = hdu[1].data['firefly_model']
	chi = np.mean(abs((data - model)/data))
	chi_arr_6.append(chi)

directory = '/users/zak/Documents/output/FireFly_eBOSS/z_0.5_0.6/CB_C6_D'

#initial arrays
chi_arr_7 = []
Z_7 = []
logAge_7 = []
Z_7_up_err=[]
Z_7_low_err=[]
for i in range(6):
	filename = '/users/zak/Documents/output/FireFly_eBOSS/z_0.5_0.6/CB_C6_D/spFly-z0506_CBC6D_V'+N[i]+'_DAP.fits'
	hdu = fits.open(filename)
	metallicity = hdu[1].header['metallicity_lightW'] #Z/H
	age = hdu[1].header['age_lightW'] #log(age/Gyr)
	Z_7_up_error = hdu[1].header['metallicity_lightW_up_1sig'] - metallicity
	Z_7_low_error = metallicity - hdu[1].header['metallicity_lightW_low_1sig']
	Z_7_up_err.append(Z_7_up_error)
	Z_7_low_err.append(Z_7_low_error)

	Z_7.append(metallicity)
	logAge_7.append(age)

	data = hdu[1].data['original_data']
	model = hdu[1].data['firefly_model']
	chi = np.mean(abs((data - model)/data))
	chi_arr_7.append(chi)
plt.errorbar(vdisp,Z_1,yerr=[Z_1_low_err,Z_1_up_err],fmt='o',elinewidth=0.9,capsize=2,color = 'navy',label='D-C2')
plt.errorbar(vdisp,Z_2,yerr=[Z_2_low_err,Z_2_up_err],fmt='o',elinewidth=0.9,capsize=2,color = 'skyblue',label='C2-2SLAQ')
plt.errorbar(vdisp,Z_3,yerr=[Z_3_low_err,Z_3_up_err],fmt='o',elinewidth=0.9,capsize=2,color='seagreen', label='2SLAQ-C3')
plt.errorbar(vdisp,Z_4,yerr=[Z_4_low_err,Z_4_up_err],fmt='o',elinewidth=0.9,capsize=2,color='olive',label='C3-LRG')
plt.errorbar(vdisp,Z_5,yerr=[Z_5_low_err,Z_5_up_err],fmt='o',elinewidth=0.9,capsize=2,color='gold',label='LRG-C5')
plt.errorbar(vdisp,Z_6,yerr=[Z_6_low_err,Z_6_up_err],fmt='o',elinewidth=0.9,capsize=2,color='orange',label='C5-C6')
plt.errorbar(vdisp,Z_7,yerr=[Z_7_low_err,Z_7_up_err],fmt='o',elinewidth=0.9,capsize=2,color='red',label='C6-D')

plt.ylim(-1.6,0.2)
plt.ylabel('Metallicity [Z/H]')
plt.xlabel('log(vdips/kms^-1)')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.title('0.5<z<0.6')
plt.show()
