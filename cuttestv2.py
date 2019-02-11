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

to do, create two arrays, (look at phone pic) where you give each colour bin a value (1,2,3,4...) and each vdisp bin a 
value(1,2,3,4...) and then for each loop, add to an array with the value for the bin its in i.e, (1,1,1,1...) for colour
as its fixed then another like (1,1,1,2,2,2...) for the vdisp 

alternatively create two arrays one for colour and one for vdisp that is such (1,1,1,1...) for colour and (1,2,3,4..) 
vdisp where each colour bin has however many vdisp bins. and a third array with the total numnber in each of those.

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
hdu = fits.open('/Users/zak/Documents/project/eBOSSMerged2.fits') 
plate_in = hdu[1].data['PLATE']
mjd_in = hdu[1].data['MJD']
fiberid_in = hdu[1].data['FIBERID']
z_in = hdu[1].data['Z']
vdisp_in = hdu[1].data['VDISP']
SN_in = hdu[1].data['SN_MEDIAN_ALL']
g_in = hdu[1].data['g']
r_in = hdu[1].data['r']
i_in = hdu[1].data['i']


z_r1 = 0.6
z_r2 = 0.7

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
	   	total1.append(len(plate))
	   	v_r1 = v_r1 + 0.05
	   	v_r2 = v_r2 + 0.05


	if np.all(i == 2): #c2-SLAQ
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
	   	total1.append(len(plate))
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
	   	total1.append(len(plate))
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
	   	total1.append(len(plate))
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
	   	total1.append(len(plate))
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
	   	total1.append(len(plate))
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
	   	total1.append(len(plate))
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
	   	total1.append(len(plate))
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
	   	total1.append(len(plate))
	   	v_r1 = v_r1 + 0.05
	   	v_r2 = v_r2 + 0.05


velarr= [1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11,12,]
colarr=[]
num = 1 
total1=np.log10(total1)
total1=np.ma.array(total1)
total_masked = np.ma.masked_where(total1>1.69897000434,total1)
for i in range(10):
	for j in range(12):
		colarr.append(num)
	num = num+1

print(velarr)
'''
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
'''
#plt.legend(bbox_to_anchor=(1.04,1))
cm = plt.cm.get_cmap('autumn')
cm_2 = plt.cm.get_cmap('winter')
sc = plt.scatter(velarr,colarr, c=total1, s=650, marker='s', cmap=cm)
cbar = plt.colorbar(sc)
sc_2=plt.scatter(velarr,colarr, c=total_masked,s=650,marker ='s', cmap=cm_2 )
cbar_2 =plt.colorbar(sc_2)

plt.xticks(np.arange(13),('','1.90-1.95','1.95-2.00','2.00-2.05','2.05-2.10','2.10-2.15','2.15-2.20','2.20-2.25','2.25-2.30','2.30-2.35','2.35-2.40','2.40-2.45','2.45-2.50'), rotation=80)
plt.yticks(np.arange(11),('','D-C1','C1-C2','C2-SLAQ','SLAQ-C3','C3-M11','M11-LRG','LRG-C5','C5-C6','C6-C7','C7-D'))
plt.xlabel('Velocity dispertion bins')
plt.ylabel('Colour bins')
plt.title('Number plot for 0.6 < z < 0.7')
#plt.ylim(0,50)
plt.savefig('selectiontestV20.4_0.5.png')
plt.show()

