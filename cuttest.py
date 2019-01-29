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


vdisp from 1.9 to 2.5 in 0.05 range 

plot number of galaxies against vdisp for each colour bin at a given redshift so an individual plot for each redshift 
containing a plot for each colour bin 

try number density plot with colour on the y and vdisp on the x with number as the density 
colour on the y will just be bin 1,2,3, etc for each segment 

if statement! 
'''

#constants for stacking 
minlam = 3.4771
maxlam = 3.7446

step_size = 0.0001
array_length = int((maxlam-minlam)/step_size)

flux_array = np.arange(minlam,maxlam,step_size)
#print(np.shape(flux_array))

interp_array = np.arange(minlam,maxlam,step_size) #array of x co-ordinates for interp values (common wavelength grid)

var_array = np.arange(minlam,maxlam,step_size) 
error_array = np.arange(minlam,maxlam,step_size)
number_stacked = 0

#bin creation
hdu = fits.open('/Users/zak/Documents/project/eBOSSMerged.fits') 
plate_in = hdu[1].data['PLATE']
mjd_in = hdu[1].data['MJD']
fiberid_in = hdu[1].data['FIBERID']
z_in = hdu[1].data['Z']
vdisp_in = hdu[1].data['VDISP']
SN_in = hdu[1].data['SN_MEDIAN_ALL']
g_in = hdu[1].data['g']
r_in = hdu[1].data['r']
i_in = hdu[1].data['i']


z_r1 = 0.8
z_r2 = 0.9

total1=[]
total2=[]
total3=[]
total4=[]
total5=[]
total6=[]
total7=[]
total8=[]
total9=[]
total10=[]

loop = [0,1,2,3,4,5,6,7,8,9]
for i in range(10):
	if np.all(i == 0): #D-c1
	   v_r1 = 1.9
	   v_r2 = 1.95

	   for j in range(12):

	   	N = ['1','2','3','4','5','6','7','8','9','10','11','12']
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
	   	#print(len(SN))

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
	   	#print(len(SN))

	   	vdisp = np.log10(vdisp)
	   	#binning, these limits can change
	   	index2 = np.where(np.logical_and((r-i) >= ((0.55)+(g-r)/8),((r-i) <= 0.72)))
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

	   	#print(len(plate))
	   	total1.append(len(plate))

	   	v_r1 = v_r1 + 0.05
	   	v_r2 = v_r2 + 0.05


	if np.all(i == 1): #c1-c2
	   v_r1 = 1.9
	   v_r2 = 1.95
	   total2=[]

	   for j in range(12):

	   	N = ['1','2','3','4','5','6','7','8','9','10','11','12']
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
	   	#print(len(SN))

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
	   	#print(len(SN))

	   	vdisp = np.log10(vdisp)
	   	#binning, these limits can change
	   	index2 = np.where(np.logical_and((r-i) >= 0.72,((r-i) <= (-0.245)*(g-r)+1.05)))
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

	   	#print(len(plate))
	   	total2.append(len(plate))
	   	v_r1 = v_r1 + 0.05
	   	v_r2 = v_r2 + 0.05
	   	print(total2)


	if np.all(i == 2): #c3-SLAQ
	   v_r1 = 1.9
	   v_r2 = 1.95

	   for j in range(12):

	   	N = ['1','2','3','4','5','6','7','8','9','10','11','12']
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
	   	#print(len(SN))

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
	   	#print(len(SN))

	   	vdisp = np.log10(vdisp)
	   	#binning, these limits can change
	   	index2 = np.where(np.logical_and((r-i) >= (-0.245)*(g-r)+1.05,((r-i) <= ((-0.7*(g-r)+1.6)/1.2)+0.18 )))
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

	   	#print(len(plate))
	   	total3.append(len(plate))
	   	v_r1 = v_r1 + 0.05
	   	v_r2 = v_r2 + 0.05

	if np.all(i == 3): #SLAQ - c3
	   v_r1 = 1.9
	   v_r2 = 1.95

	   for j in range(12):

	   	N = ['1','2','3','4','5','6','7','8','9','10','11','12']
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
	   	#print(len(SN))

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
	   	#print(len(SN))

	   	vdisp = np.log10(vdisp)
	   	#binning, these limits can change
	   	index2 = np.where(np.logical_and((r-i) >= ((-0.7*(g-r)+1.6)/1.2)+0.18 ,((r-i) <= (-1.8)*(g-r)+3.16 )))
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

	   	#print(len(plate))
	   	total4.append(len(plate))
	   	v_r1 = v_r1 + 0.05
	   	v_r2 = v_r2 + 0.05

	if np.all(i == 4): #c3 - m11
	   v_r1 = 1.9
	   v_r2 = 1.95

	   for j in range(12):

	   	N = ['1','2','3','4','5','6','7','8','9','10','11','12']
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
	   	#print(len(SN))

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
	   	#print(len(SN))

	   	vdisp = np.log10(vdisp)
	   	#binning, these limits can change
	   	index2 = np.where(np.logical_and((r-i) >= (-1.8)*(g-r)+3.16 ,((r-i) <= (-(g-r))+2.35)))
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

	   	#print(len(plate))
	   	total5.append(len(plate))
	   	v_r1 = v_r1 + 0.05
	   	v_r2 = v_r2 + 0.05


	if np.all(i == 5): #m11-lrg 
	   v_r1 = 1.9
	   v_r2 = 1.95

	   for j in range(12):

	   	N = ['1','2','3','4','5','6','7','8','9','10','11','12']
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
	   	#print(len(SN))

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
	   	#print(len(SN))

	   	vdisp = np.log10(vdisp)
	   	#binning, these limits can change
	   	index2 = np.where(np.logical_and((r-i) >= (-(g-r))+2.35 ,((r-i) >= 4*((g-r)-1.3))))
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

	   	#print(len(plate))
	   	total6.append(len(plate))
	   	v_r1 = v_r1 + 0.05
	   	v_r2 = v_r2 + 0.05

	if np.all(i == 6): #lrg-c5
	   v_r1 = 1.9
	   v_r2 = 1.95

	   for j in range(12):

	   	N = ['1','2','3','4','5','6','7','8','9','10','11','12']
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
	   	#print(len(SN))

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
	   	#print(len(SN))

	   	vdisp = np.log10(vdisp)
	   	#binning, these limits can change
	   	index2 = np.where(np.logical_and((r-i) <= 4*((g-r)-1.3) ,((r-i) >= (1.5)*(g-r)-1.49)))
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

	   	#print(len(plate))
	   	total7.append(len(plate))
	   	v_r1 = v_r1 + 0.05
	   	v_r2 = v_r2 + 0.05


	if np.all(i == 7): #c5-c6
	   v_r1 = 1.9
	   v_r2 = 1.95

	   for j in range(12):

	   	N = ['1','2','3','4','5','6','7','8','9','10','11','12']
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
	   	#print(len(SN))

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
	   	#print(len(SN))

	   	vdisp = np.log10(vdisp)
	   	#binning, these limits can change
	   	index2 = np.where(np.logical_and((r-i) <= (1.5)*(g-r)-1.49 ,((r-i) >= (0.5)*(g-r)-0.013)))
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

	   	#print(len(plate))
	   	total8.append(len(plate))
	   	v_r1 = v_r1 + 0.05
	   	v_r2 = v_r2 + 0.05

	if np.all(i == 8): #c6-c7
	   v_r1 = 1.9
	   v_r2 = 1.95

	   for j in range(12):

	   	N = ['1','2','3','4','5','6','7','8','9','10','11','12']
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
	   	#print(len(SN))

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
	   	#print(len(SN))

	   	vdisp = np.log10(vdisp)
	   	#binning, these limits can change
	   	index2 = np.where(np.logical_and((r-i) <= (0.5)*(g-r)-0.013 ,((r-i) >= (0.3)*(g-r)+0.284)))
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

	   	#print(len(plate))
	   	total9.append(len(plate))
	   	v_r1 = v_r1 + 0.05
	   	v_r2 = v_r2 + 0.05

	if np.all(i == 9): #c7-D
	   v_r1 = 1.9
	   v_r2 = 1.95

	   for j in range(12):

	   	N = ['1','2','3','4','5','6','7','8','9','10','11','12']
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
	   	#print(len(SN))

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
	   	#print(len(SN))

	   	vdisp = np.log10(vdisp)
	   	#binning, these limits can change
	   	index2 = np.where(np.logical_and((r-i) <= (0.3)*(g-r)+0.284 ,((r-i) >= 0.55+((g-r)/8))))
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

	   	#print(len(plate))
	   	total10.append(len(plate))
	   	v_r1 = v_r1 + 0.05
	   	v_r2 = v_r2 + 0.05


velarr=[1,2,3,4,5,6,7,8,9,10,11,12]
print(velarr)
print(total2)
plt.figure(figsize=(15,15))

plt.plot(velarr,total1,label='D-C1')
plt.plot(velarr,total2,label='C1-C2')
plt.plot(velarr,total3,label='C2-SLAQ')
plt.plot(velarr,total4,label='SLAQ-C3')
plt.plot(velarr,total5,label='C3-M11')
plt.plot(velarr,total6,label='M11-LRG')
plt.plot(velarr,total7,label='LRG-C5')
plt.plot(velarr,total8,label='C5-C6')
plt.plot(velarr,total9,label='C6-C7')
plt.plot(velarr,total10,label='C7-D')

plt.legend(bbox_to_anchor=(1.04,1))
plt.xticks(np.arange(1,13))
plt.xlabel('velocity dispertion bins')
plt.ylabel('number of galaxies')
plt.title('Number plot for 0.8 < z < 0.9')
plt.ylim(0,50)
plt.savefig('selectiontest0.8_0.9.png')
plt.show()

