import os 
import sys, os.path
import numpy as np
from astropy.io import fits
import matplotlib ; matplotlib.use('Agg')
from matplotlib import pyplot as plt
import matplotlib.mlab as mlab
import pylab
import glob
import gc



directory = '/mnt/lustre/sdss-dr12/eBOSS-DR16/spectra/7835'

#creating array to store Z values

z_values = []

allfits = glob.glob(directory+'/*.fits') #opening up all files in directior with .fits extention

for filename in allfits:
	print(filename)
	hdu = fits.open(filename)
	objtype = hdu[2].data["OBJTYPE"]

	if objtype == 'GALAXY':
		redshift = hdu[2].data["Z"]
		print(redshift)
		z_values.append(redshift)

	hdu.close() #closing the .fits file
	del hdu[2].data #closing the memmap data

	gc.collect() #making sure python cleans up 

print(z_values)
print("The max redshift is ",max(z_values))
print("The min redshift is ",min(z_values))

hist, bin_edges = np.histogram(z_values,bins=500)
#print(np.size(hist))
#print(np.size(bin_edges))

bin_center= ((bin_edges[:-1] + bin_edges[1:])/2)

val = float(np.max(hist))
y = hist

plt.plot(bin_center, y, 'k')
plt.xlim(0,1.5)
plt.ylim(0,30)
plt.xlabel("Redshift")
plt.ylabel("Frequency")
plt.title("Histogram of Redshift for Fiberid 7835")



plt.savefig('redshift7835galaxyonly.pdf')

