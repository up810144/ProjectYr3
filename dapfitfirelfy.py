#Besides the standard useful Python packages, we need to downlad the specific Firefly packages. 
import sys, os.path
import numpy as np
import astropy.cosmology as co
import GalaxySpectrumFIREFLY as gs
import StellarPopulationModel as spm
from astropy.io import fits
from matplotlib import pyplot as plt
#matplotlib notebook

#GalaxySpectrumFIREFLY Loads the environnement to transform observed spectra into the input for FIREFLY. The cosmology needs to be set:

cosmo=co.Planck13
print cosmo

#We have an example spectra from the SDSS, which name contain the Plate number and MJD and Fiber ids.
N = ['1','2','3','4','5','6']

for i in range(6):

    file_path = '/Users/zak/Documents/project/DAP_Stacks/z_0.8_0.9/CB_SLAQ_C3/z0809_CBSLAQC3_V'+N[i]+'_DAP.fits'

    # Check that the file actually exists
    if (not os.path.isfile(file_path)):
        print 'Not found: ', file_path
        sys.exit()



    #We pass the path to this file to GalaxySpectrumFIREFLY and we set this module to use the Milky Way reddening maps:

    spec=gs.GalaxySpectrumFIREFLY(file_path, milky_way_reddening=True)
    print type(spec)

    #We set GalaxySpectrumFIREFLY and is set to read different formats of files with spectra: MaNGA, DEEP2, stacked for eBOSS, model from Illustris, etc. (see the complete documentation for more details).
    spec.stack_no_lines()
    print spec.ra,spec.dec
    print spec.restframe_wavelength

    #At the moment Firefly has only spectral templates for galaxies and star clusters. Below we check if we actually have the spectra of an SDSS galaxy and if it's redshift is adecuatelly determined:
    #zz= spec.redshift ; print zz
    #if ((spec.hdulist[2].data['CLASS'][0]!="GALAXY")) or \
    #    (zz <=  spec.hdulist[2].data['Z_ERR'][0]) or \
    #    (spec.hdulist[2].data['Z_ERR'][0]<0) or \
    #    (spec.hdulist[2].data['ZWARNING'][0] !=0):
    #   print 'This is either not a galaxy or it has a poorly determined redshift.'
    #   sys.exit()

    #Firefly has spectra templates in a range of ages and metalliticities that depend on your choice of stellar libraries. The default age and metallicity ranges are set in linear units. If you want to restrict your minimisation further, make sure that you include these new limits also in linear units, as at the moment the code won't deal properly with logarithmic limits. Let's set the new age and metallicity limits for our run.

    ageMin = 0.
    ageMax = 15 #changed to fixed value #np.log10(cosmo.age(zz).value*1e9) #Gyr
    ZMin = 0.001 #[Z/H]
    ZMax = 4. 

    #The next step is to choose the stellar population model, stellar library and IMF. The directory 'stellar_population_model' containes all the provided options and further details are in the documentation.

    model = 'm11'      # Maraston & Stromback 2011
    library = 'MILES' # Prugniel et al. 2007. #played with different libs 
    imf = 'cha'        # Chabrier 2003

    #We set up now an output file. Note that the created directory 'output' is not tracked by git, so you won't see it in your directory, however it'll be created if you follow the commands presented here in your own script.
    outputdir = '../output/'
    if not os.path.exists(outputdir):
        os.makedirs(outputdir)

    # Take part of the name of the input file for the output
    outputfile = outputdir+'spFly-'+ os.path.basename(file_path)[:-5]+'.fits'
    print outputfile

    #Let's populate the header of the output file with all the relevant information, making use of the StellarPopulationModel:
    prihdr = spm.pyfits.Header()
    prihdr['FILE']          = os.path.basename(outputfile)
    #prihdr['PLATE']         = plate 
    #prihdr['MJD']           = mjd   
    #prihdr['FIBERID']       = fiber 
    prihdr['MODELS']        = model
    prihdr['FITTER']        = "FIREFLY"
    #prihdr['AGEMIN']        = str(ageMin)
    #prihdr['AGEMAX']        = str(ageMax)
    prihdr['ZMIN']          = str(ZMin)
    prihdr['ZMAX']          = str(ZMax)
    #prihdr['redshift']      = zz
    prihdu = spm.pyfits.PrimaryHDU(header=prihdr)

    #We are going to run Firefly with the downgrade template libraries, 'use_downgraded_models = True'. You can downgrade the spectral templates to the resolution you need by setting 'downgrade_models = True', note that this is a long process.
    tables = [prihdu]
    try :
        bestfit = spm.StellarPopulationModel(spec, outputfile, cosmo, models = model, \
                                             model_libs = [library], imfs = [imf], \
                                             age_limits = [ageMin,ageMax], \
                                             downgrade_models = False, \
                                             data_wave_medium = 'vacuum', \
                                             Z_limits = [ZMin,ZMax], \
                                             use_downgraded_models = True, write_results = False)
        bestfit.fit_models_to_data()
        tables.append(bestfit.tbhdu )
        converged = True
    except (ValueError):
        tables.append(bestfit.create_dummy_hdu())
        converged = False

    #The Firefly best fits will be stored as tables only if the fit converges.
    if converged :
        complete_hdus = spm.pyfits.HDUList(tables)
        if os.path.isfile(outputfile):
            os.remove(outputfile)
        complete_hdus.writeto(outputfile)
'''
    #Let's plot the best fit compared together with the original spectrum:
    # Get the relevant data from the file
    header =  fits.open(outputfile)  ; thefit = 1
    wavelength = header[thefit].data['wavelength']
    original_flux = header[thefit].data['original_data']
    bestfit_model = header[thefit].data['firefly_model']
    # Plot the spectra
    plt.plot(wavelength, original_flux, 'k')
    plt.plot(wavelength, bestfit_model, 'r')

    # Add labels and tick marks
    plt.ylabel("flux (1e-17erg/cm^2/s/Ang)")
    plt.xlabel("wavelength (Angstrom)")
    plt.title("Firefly fit of 0.5 to 0.6 Z dap fit spectra using MILES library")
    #xtit = ('Wavelength (%s)' % header[thefit].header['TUNIT1'])
    #ytit = ('Flux (%s)' % header[thefit].header['TUNIT2'])
    #fn = 22 ; plt.xlabel(xtit, fontsize=fn) ; plt.ylabel(ytit, fontsize=fn)
    #plt.tick_params(axis='both', which='major', labelsize=fn)
    plt.show()
'''
