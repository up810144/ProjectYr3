import matplotlib
matplotlib.use('agg')
from matplotlib import pyplot as plt
import numpy as np
import os
from astropy.io import fits
from matplotlib import rcParams
import random
from mangadap.proc.templatelibrary import TemplateLibrary
from mangadap.proc.ppxffit import PPXFFit
from mangadap.proc.stellarcontinuummodel import StellarContinuumModelBitMask
from mangadap.util.instrument import spectrum_velocity_scale, resample_vector, match_spectral_resolution, SpectralResolution, spectral_coordinate_step
from mangadap.par.emissionlinedb import EmissionLineDB
from mangadap.proc.elric import Elric
from mangadap.proc.emissionlinemodel import EmissionLineModelBitMask
import astropy.constants as const

#Plotting settings
params = {'axes.labelsize': 20, 'axes.titlesize':20, 'font.size': 16, 'legend.fontsize': 16,
            'xtick.labelsize': 16, 'ytick.labelsize': 16}
rcParams.update(params)
rcParams['xtick.major.pad'] = 8
rcParams['ytick.major.pad'] = 8

#Initialising 
dapsrc=os.environ['MANGADAP_DIR']
em_line_db = EmissionLineDB('ELPFULL')                          #ELPSTRONG used previously; ELPEXTENDED contains way more lines
mask = EmissionLineModelBitMask()
spec = PPXFFit(StellarContinuumModelBitMask(dapsrc=dapsrc))
fitter = Elric(mask)

N = ['1','2','3','4','5','6','7','8','9','10']

for i in range(0,10):

	#Read in your datafile here to get wavelength, flux, error, spectral resolution, redshift...
	file_path = "/users/zt810144/project/TestStacks/zvdisp_teststack"+N[i]+".fits"
	hdu = fits.open(file_path)
	wavelength = 10**hdu[1].data
	flux = hdu[2].data.reshape(1,-1)
	error = hdu[3].data.reshape(1,-1)
	redshift = 0. #zero as stack is deredshiftd
	sigma = 100. #guess velocity dispertion
	meanWL = (wavelength[1:]+wavelength[:-1])/2. 
	deltaWL = wavelength[1:]-wavelength[:-1]
	sres = np.ones_like(wavelength)*np.mean(meanWL / deltaWL)

	###################

	spectral_step = spectral_coordinate_step(wavelength, log=True)

	#Create template library, to be used for fitting; hardcopy=False means that no files will be saved
	tpl = TemplateLibrary('MILESHC', dapsrc=dapsrc, quiet=True, spectral_step=spectral_step, log=True, process=True,
	                      hardcopy=False, directory_path='.', processed_file='test.fits', velscale_ratio=4)

	#guess_dispersion can be set to e.g. 70km/s
	model_wave, model_flux, model_mask, model_par = spec.fit(tpl['wave'].data, tpl['flux'].data, wavelength, flux, error,		
	                                                         guess_redshift=redshift, guess_dispersion=sigma, quiet=True, mask=None, iteration_mode = 'no_global_wrej',
	                                                         matched_resolution=False, tpl_sres=tpl['wave'].data/2.5, obj_sres=sres, velscale_ratio=4)        #2.5 for MILESHC



	fitted_sig = model_par['KIN'][:,1] # fitted velocity disp
	fitted_sig_err  = model_par['KINERR'][:,1] #error in fitted vel disp

	#sigma_corrected = np.ma.sqrt(np.square(fitted_sig) - np.square(model_par['SIGMACORR_EMP'])).filled(0.0)

	model_wave_em, model_flux_em, model_base, model_mask_em, model_fit_par, model_eml_par = fitter.fit(wavelength, flux-model_flux, em_line_db, ivar = 1./np.square(error),
	                                            mask=None, continuum=None, sres=sres, base_order=0, guess_redshift=np.array([0.0]), guess_dispersion=fitted_sig, quiet=True)
	fitted_flux = flux-model_flux_em



	new_hdu = fits.HDUList()
	Phdr = fits.Header()
	new_hdu.append(fits.PrimaryHDU(header=Phdr))
	new_hdu.append(fits.ImageHDU(data=wavelength, name='wavelength'))
	new_hdu.append(fits.ImageHDU(data=fitted_flux.reshape(-1), name='flux'))
	new_hdu.append(fits.ImageHDU(data=error.reshape(-1), name='error'))
	new_hdu.append(fits.ImageHDU(data=fitted_sig, name='vdisp'))


	new_hdu.writeto("zvdisp_teststackdapfit"+N[i]+".fits", overwrite=True)




	plt.plot(wavelength, flux[0], 'black')
	plt.plot(wavelength, model_flux[0], 'red')
	plt.plot(wavelength, model_flux_em[0], 'green')
	plt.plot(wavelength,fitted_flux[0],'blue')
	plt.ylabel("flux (1e-17erg/cm^2/s/Ang)")
	plt.xlabel("wavelength (Angstrom)")
	plt.show()
	plt.savefig('zvdisp_teststackdapfit'+N[i]+'.png')
