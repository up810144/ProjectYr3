import sys, os.path
import numpy as np
from astropy.io import fits
from matplotlib import pyplot as plt


file_path = '/users/zak/Documents/project/z0405_CBC2SLAQ_V4_DAP.fits'

# Check that the file actually exists

if (not os.path.isfile(file_path)):
    print('Not found: ', file_path)
    sys.exit()

# Print the content of the file

hdu =  fits.open(file_path)


flux = hdu[2].data
print("flux array = ",flux)

print("min flux = ", max(flux))
print("max flux = ", min(flux))


wavelength = hdu[1].data
print("The wavelength array is:",wavelength)
print("max wavelength = ",max(wavelength))
print("min wavelength = ",min(wavelength))


#error 

error = hdu[3].data

#vdisp = hdu[4].data

#mean_error = hdu[3].data

'''
#plotting flux against wavelength and flux against restframe

plt.plot((10**wavelength), flux, 'k')

#comment out which error you dont want to plot
#plt.fill_between((10**wavelength),flux-mean_error,flux+mean_error, color = 'r', alpha=0.6)

plt.fill_between((10**wavelength),flux-error,flux+error, color = 'b')

#plt.fill_between((10**wavelength),flux-mean_error,flux+mean_error, color = 'r', alpha=0.6)



#formatting figure
#plt.ylim(-8,8)
#plt.xlim(10**0.3,10**0.8)
#plt.title("Stacked spectra of plate 7835 with median error")
plt.ylabel("flux (1e-17erg/cm^2/s/Ang)")
plt.xlabel("wavelength (Angstrom)")

plt.show()
'''


plt.plot(wavelength, flux, 'black')

plt.ylabel("flux (1e-17erg/cm^2/s/Ang)")
plt.xlabel("wavelength (Angstrom)")
plt.show()