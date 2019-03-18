import sys, os.path
import numpy as np
from astropy.io import fits
from matplotlib import pyplot as plt

file_path = '/users/zak/Documents/output/FireFly_eBOSS/z_0.4_0.5/CB_C2_SLAQ/spFly-z0405_CBC2SLAQ_V1_DAP.fits'

# Check that the file actually exists

if (not os.path.isfile(file_path)):
    print('Not found: ', file_path)
    sys.exit()
# Print the content of the file

hdu =  fits.open(file_path)

wavelength = hdu[1].data['wavelength']
original_flux = hdu[1].data['original_data']
bestfit_model = hdu[1].data['firefly_model']

plt.plot(wavelength, original_flux, 'k')
plt.plot(wavelength, bestfit_model, 'r')

# Add labels and tick marks
plt.ylabel("flux (1e-17erg/cm^2/s/Ang)")
plt.xlabel("wavelength (Angstrom)")

plt.show()
