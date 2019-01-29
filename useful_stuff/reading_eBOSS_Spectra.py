import sys, os.path
import numpy as np
from astropy.io import fits
from matplotlib import pyplot as plt


file_path = '/users/zak/Documents/placement/eBOSS_plates/7835/spec-7835-56986-0470.fits'

# Check that the file actually exists

if (not os.path.isfile(file_path)):
    print('Not found: ', file_path)
    sys.exit()

# Print the content of the file

hdu =  fits.open(file_path)
#hdu.info()

# Print the global information of the eBOSS spectra

#list_of_keys = hdu[0].header.keys()
#for key in list_of_keys:
        #print (key,' = ',hdu[0].header[key])


# printing flux, wavelength etc (NOTE: values are logged as in 10**A where A is the value in array)

flux = hdu[1].data['flux']
print("flux array = ",flux)

print(max(flux))
print(min(flux))


wavelength = hdu[1].data['loglam']

print("The wavelength array is:",wavelength)
print("max wavelength = ",max(wavelength))
print("min wavelength = ",min(wavelength))

redshift = hdu[2].data["Z"]

print("The Redshift is ", redshift)

#calculating restframe wavelength

restframe = (10**wavelength)/(1+redshift)
print(max(restframe))
print(min(restframe))

logRestframe = wavelength/(1+redshift) #restframe logged
print(len(logRestframe))
##interpolation

#constants
minlam = 3.3754
maxlam = 3.7839

step_size = 0.0001
array_length = (maxlam-minlam)/step_size

interp_array = np.arange(minlam,maxlam,step_size) #array of x co-ordinates for interp values
print(interp_array)
print(len(interp_array))

interp_flux = np.interp((10**interp_array),restframe,flux)
print(interp_flux)
print(len(interp_flux))

# naming convention 

plateid = hdu[0].header["PLATEID"]
mjd = hdu[0].header["MJD"]
fiberid = hdu[0].header["FIBERID"]

#plotting flux against wavelength and flux against restframe

plt.plot((10**wavelength), flux, 'b', label="With redshift")

plt.plot((restframe),flux, 'r', label="restframe")
plt.plot((10**interp_array),(interp_flux), 'k',label="Interplated")
#formatting figure
#plt.ylim(-8,8)
#plt.xlim(10**0.3,10**0.8)
plt.title("Specrta of spec-"+str(plateid)+"-"+str(mjd)+"-"+str(fiberid)+" at Rest-Frame")
plt.ylabel("flux (1e-17erg/cm^2/s/Ang)")
plt.xlabel("wavelength (Angstrom)")
plt.legend()
plt.show()