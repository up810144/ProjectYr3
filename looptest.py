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
do histogram of vdisp in log - max vdsip is 350 hardcap above 0 
create a selection loop that can loop through and stack (if we have low numbers to stack)
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
hdu = fits.open('/users/zt810144/project/eBOSSMerged.fits') 
plate_in = hdu[1].data['PLATE']
mjd_in = hdu[1].data['MJD']
fiberid_in = hdu[1].data['FIBERID']
z_in = hdu[1].data['Z']
vdisp_in = hdu[1].data['VDISP']
SN_in = hdu[1].data['SN_MEDIAN_ALL']
g_in = hdu[1].data['g']
r_in = hdu[1].data['r']
i_in = hdu[1].data['i']

#vdisp_in=np.log10(vdisp_in)

z_r1 = 0.3
z_r2 = 0.4
v_r1 = 2
v_r2 = 2.05

N = ['1','2','3','4','5','6','7','8','9','10']

for j in range(0,10):

	#initial indexing with absolute limits (i.e. this will not change)
	index = np.where(SN_in>=2)
	SN = SN_in[index]
	z = z_in[index]
	vdisp = vdisp_in[index]
	plate = plate_in[index]
	mjd = mjd_in[index]
	fiberid = fiberid_in[index]
	g = g_in[index]
	r = r_in[index]
	i = i_in[index]
	print(len(SN))

	index5 = np.where(np.logical_and(vdisp>0,vdisp<350))
	SN = SN[index5]
	z = z[index5]
	vdisp = vdisp[index5]
	plate = plate[index5]
	mjd = mjd[index5]
	fiberid = fiberid[index5]
	g = g[index5]
	r = r[index5]
	i = i[index5]
	print(len(SN))

	vdisp = np.log10(vdisp)

	#binning, these limits can change

	index2 = np.where(np.logical_and(((r-i) <= (((1.5)*(g-r))-1.49)),((r-i) >= 0.5*(g-r)-0.013)))
	SN = SN[index2]
	z = z[index2]
	vdisp = vdisp[index2]
	plate = plate[index2]
	mjd = mjd[index2]
	fiberid = fiberid[index2]
	g = g[index2]
	r = r[index2]
	i = i[index2]
	#print(g)


	index3 = np.where(np.logical_and(z>z_r1,z<z_r2))
	SN = SN[index3]
	z = z[index3]
	vdisp = vdisp[index3]
	plate = plate[index3]
	mjd = mjd[index3]
	fiberid = fiberid[index3]
	g = g[index3]
	r = r[index3]
	i = i[index3]

	index4 = np.where(np.logical_and(vdisp>v_r1,vdisp<v_r2))
	SN = SN[index4]
	z = z[index4]
	vdisp = vdisp[index4]
	plate = plate[index4]
	mjd = mjd[index4]
	fiberid = fiberid[index4]
	g = g[index4]
	r = r[index4]
	i = i[index4]

	#converting each np array into an array of strings 
	plate = list(map(str,plate))
	mjd = list(map(str,mjd))
	fiberid = list(map(str,fiberid))

	print(len(plate))


	for i in range(0,len(plate)):
		path = '/mnt/lustre/sdss-dr12/eBOSS-DR14/spectra/' + plate[i] +'/spec-'+plate[i]+'-'+mjd[i]+'-'+fiberid[i].zfill(4)+'.fits'
		hdu = fits.open(path)
		redshift = hdu[2].data['Z']
		wavelength = hdu[1].data['loglam']
		#print(len(wavelength))
		flux = hdu[1].data["flux"]
		#ivar = hdu[1].data["ivar"]**-1 #variance 
		#if ivar > 0:
		#	var = ivar**-1
		restframe = (10**wavelength)/(1+redshift) #removing redshift
		interp_flux = np.interp((10**interp_array),restframe,flux) #interpolating to common wavelength grid
		#interp_var = np.interp((10**interp_array),restframe,var)
		flux_array = np.vstack((flux_array,interp_flux,)) #stacking the flux arrays
		#var_array = var_array + interp_var
		number_stacked +=1 
		hdu.close()


	#mean_error = np.sqrt(var_array)/number_stacked #propergated erro
	#print("the error array is: ",mean_error)

	sort_flux = np.sort(flux_array, axis=0)

	median_flux = np.median(sort_flux, axis=0)

	standard_dev = np.std(sort_flux, axis=0) 

	new_error = 1.25 * (standard_dev/np.sqrt(number_stacked))

	#print(new_error)

	new_hdu = fits.HDUList()
	Phdr = fits.Header()
	new_hdu.append(fits.PrimaryHDU(header=Phdr))
	new_hdu.append(fits.ImageHDU(data=interp_array, name='wavelength'))
	new_hdu.append(fits.ImageHDU(data=median_flux, name='flux'))
	#new_hdu.append(fits.ImageHDU(data=mean_error, name='mean_error'))
	new_hdu.append(fits.ImageHDU(data=new_error, name='error'))


	new_hdu.writeto("zvdisp_teststack"+N[j]+".fits", overwrite=True)

	#hdu.writeto("7835stack.fits",clobber=True)


	plt.plot((10**interp_array),median_flux,'k')

	#plt.fill_between((10**interp_array),median_flux-mean_error,median_flux+mean_error, color = 'b')
	plt.fill_between((10**interp_array),median_flux-new_error,median_flux+new_error, color='b')

	plt.ylabel("flux (1e-17erg/cm^2/s/Ang)")
	plt.xlabel("wavelength (Angstrom)")
	plt.title("Stacked spectra of galaxies in range 0.3 < z <0.4")
	plt.savefig('zvdisp_teststack'+N[j]+'.pdf')

	v_r1 = v_r1 + 0.05
	v_r2 = v_r2 + 0.05

	#print(len(plate))


