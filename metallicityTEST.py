import os
import sys, os.path
import numpy as np
from astropy.io import fits
from matplotlib import pyplot as plt
import matplotlib.mlab as mlab
import pylab
import glob
import gc


#initial arrays
chi_arr_1 = []
Z_1 = []
logAge_1 = []
vdisp = [1.95,2.05,2.15,2.25,2.35,2.45]
N=['1','2','3','4','5','6']

flux=[]
lamda = []
data=[]
for i in range(6):
	filename = '/users/zak/Documents/output/FireFly_eBOSS/z_0.4_0.5/CB_SLAQ_C3/spFly-z0405_CBSLAQC3_V'+N[i]+'_DAP.fits'


	hdu = fits.open(filename)
	metallicity = hdu[1].header['metallicity_lightW'] #Z/H
	age = hdu[1].header['age_lightW'] #log(age/Gyr)
	lamda = hdu[1].data['wavelength']
	Z_1.append(metallicity)
	logAge_1.append(age)
	original_data = hdu[1].data['original_data']
	model = hdu[1].data['firefly_model']
	data.append(original_data)
	flux.append(model)
	chi = np.mean(abs((data - model)/data))
	chi_arr_1.append(chi)



plt.subplot(221)
plt.scatter(vdisp,Z_1)
plt.title('metallicities of 2SLAQ-C3, 0.4<z<0.5')

plt.subplot(222)
plt.scatter(vdisp,logAge_1)
plt.title('log Age of 2SLAQ-C3, 0.4<z<0.5')

plt.subplot(223)
plt.plot(lamda,data[2],'k')
plt.plot(lamda,flux[2],alpha=0.7)
plt.title('vdisp = 2.15')

plt.subplot(224)
plt.plot(lamda,flux[3],'k')
plt.plot(lamda,flux[3],alpha=0.7)
plt.title('vdisp = 2.25')

'''

plt.subplot(422)
plt.plot(lamda,data[0],'k')
plt.plot(lamda,flux[0],alpha=0.7)
plt.title('vdisp = 1.95')

plt.subplot(423)
plt.plot(lamda,data[1],'k')
plt.plot(lamda,flux[1],alpha=0.7)
plt.title('vdisp = 2.05')

plt.subplot(424)
plt.plot(lamda,data[2],'k')
plt.plot(lamda,flux[2],alpha=0.7)
plt.title('vdisp = 2.15')

plt.subplot(425)
plt.plot(lamda,flux[3],'k')
plt.plot(lamda,flux[3],alpha=0.7)
plt.title('vdisp = 2.25')

plt.subplot(426)
plt.plot(lamda,flux[4],'k')
plt.plot(lamda,flux[4],alpha=0.7)
plt.title('vdisp = 2.35')

plt.subplot(427)
plt.plot(lamda,flux[5],'k')
plt.plot(lamda,flux[5],alpha=0.7)
plt.title('vdisp = 2.45')

'''

#plt.subplots_adjust(hspace = 0.7)
plt.show()
