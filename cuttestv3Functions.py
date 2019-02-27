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

git rid of m11 cut
combine bins so D-c2 and c6-D
vdisp bin at 0.1 instead of 0.05 

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
SN_in = hdu[1].data['SN_MEDIAN_ALL']
z_in = hdu[1].data['Z']
vdisp_in = hdu[1].data['VDISP']
plate_in = hdu[1].data['PLATE']
mjd_in = hdu[1].data['MJD']
fiberid_in = hdu[1].data['FIBERID']
g_in = hdu[1].data['g']
r_in = hdu[1].data['r']
i_in = hdu[1].data['i']


z_r1 = 0.6
z_r2 = 0.7
total0=[]
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

def absolute_boundaries(SN_in,z_in,vdisp_in,plate_in,mjd_in,fiberid_in,g_in,r_in,i_in):
	
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

	   	vdisp = np.log10(vdisp)

	   	#binning, these limits can change
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


	   	return(SN,z,vdisp,plate,mjd,fiberid,g,r,i)
'''
def colour_index(index2,SN,z,vdisp,plate,mjd,fiberid,g,r,i):
		SN = SN[index2]
	   	z = z[index2]
	   	vdisp = vdisp[index2]
	   	plate = plate[index2]
	   	mjd = mjd[index2]
	   	fiberid = fiberid[index2]
	   	g = g[index2]
	   	r = r[index2]
	   	i = i[index2]
	   	return(plate)

'''
for i in range(7):
	if np.all(i == 0): #D-c2
	   v_r1 = 1.9
	   v_r2 = 2.0

	   for j in range(6):

	   	SN,z,vdisp,plate,mjd,fiberid,g,r,i = absolute_boundaries(SN_in,z_in,vdisp_in,plate_in,mjd_in,fiberid_in,g_in,r_in,i_in)

	   	#colour bin
	   	index2 = np.where(np.logical_and((r-i) >= ((0.55)+(g-r)/8),((r-i) <= (-0.245)*(g-r)+1.05)))
	   	SN = SN[index2]
	   	z = z[index2]
	   	vdisp = vdisp[index2]
	   	plate = plate[index2]
	   	mjd = mjd[index2]
	   	fiberid = fiberid[index2]
	   	g = g[index2]
	   	r = r[index2]
	   	i = i[index2]
	   	
	   	#print(len(plate))
	   	total1.append(len(plate))


	   	v_r1 = v_r1 + 0.1
	   	v_r2 = v_r2 + 0.1



	if np.all(i == 1): #c2-SLAQ
	   v_r1 = 1.9
	   v_r2 = 2.0

	   for j in range(6):

	   	SN,z,vdisp,plate,mjd,fiberid,g,r,i = absolute_boundaries(SN_in,z_in,vdisp_in,plate_in,mjd_in,fiberid_in,g_in,r_in,i_in)

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

	   	#print(len(plate))
	   	total1.append(len(plate))
	   	total2.append(len(plate))
	   	v_r1 = v_r1 + 0.1
	   	v_r2 = v_r2 + 0.1

	if np.all(i == 2): #SLAQ - c3
	   v_r1 = 1.9
	   v_r2 = 2.0

	   for j in range(6):

	   	SN,z,vdisp,plate,mjd,fiberid,g,r,i = absolute_boundaries(SN_in,z_in,vdisp_in,plate_in,mjd_in,fiberid_in,g_in,r_in,i_in)

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
	   	
	   	#print(len(plate))
	   	total1.append(len(plate))
	   	total3.append(len(plate))
	   	v_r1 = v_r1 + 0.1
	   	v_r2 = v_r2 + 0.1

	if np.all(i == 3): #c3 - LRG
	   v_r1 = 1.9
	   v_r2 = 2.0

	   for j in range(6):

	   	SN,z,vdisp,plate,mjd,fiberid,g,r,i = absolute_boundaries(SN_in,z_in,vdisp_in,plate_in,mjd_in,fiberid_in,g_in,r_in,i_in)


	   	#binning, these limits can change
	   	index2 = np.where(((r-i) >= (-1.8)*(g-r)+3.16) & ((r-i) >= 4*((g-r)-1.3))&((r-i) >= ((0.55)+(g-r)/8)))
	   	z = z[index2]
	   	vdisp = vdisp[index2]
	   	plate = plate[index2]
	   	mjd = mjd[index2]
	   	fiberid = fiberid[index2]
	   	g = g[index2]
	   	r = r[index2]
	   	i = i[index2]
	   	
	   	#print(len(plate))
	   	total1.append(len(plate))
	   	total4.append(len(plate))
	   	v_r1 = v_r1 + 0.1
	   	v_r2 = v_r2 + 0.1


	if np.all(i == 4): #lrg-c5
	   v_r1 = 1.9
	   v_r2 = 2.0

	   for j in range(6):

	   	
	   	SN,z,vdisp,plate,mjd,fiberid,g,r,i = absolute_boundaries(SN_in,z_in,vdisp_in,plate_in,mjd_in,fiberid_in,g_in,r_in,i_in)


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

	   	#print(len(plate))
	   	total1.append(len(plate))
	   	total6.append(len(plate))
	   	v_r1 = v_r1 + 0.1
	   	v_r2 = v_r2 + 0.1


	if np.all(i == 5): #c5-c6
	   v_r1 = 1.9
	   v_r2 = 2.0

	   for j in range(6):

	    SN,z,vdisp,plate,mjd,fiberid,g,r,i = absolute_boundaries(SN_in,z_in,vdisp_in,plate_in,mjd_in,fiberid_in,g_in,r_in,i_in)

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

	    #print(len(plate))
	    total1.append(len(plate))
	    total7.append(len(plate))
	    v_r1 = v_r1 + 0.1
	    v_r2 = v_r2 + 0.1

	if np.all(i == 6): #c6-c7
	   v_r1 = 1.9
	   v_r2 = 2.0

	   for j in range(6):

	   	SN,z,vdisp,plate,mjd,fiberid,g,r,i = absolute_boundaries(SN_in,z_in,vdisp_in,plate_in,mjd_in,fiberid_in,g_in,r_in,i_in)


	   	#binning, these limits can change
	   	index2 = np.where(np.logical_and((r-i) <= (0.5)*(g-r)-0.013 ,((r-i) >= 0.55+((g-r)/8))))
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

	 
	   	#print(len(plate))
	   	total1.append(len(plate))
	   	total8.append(len(plate))
	   	v_r1 = v_r1 + 0.1
	   	v_r2 = v_r2 + 0.1

	


velarr= [1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6]
colarr=[]
num = 1 
total1=np.log10(total1)
total1=np.ma.array(total1)
total_masked = np.ma.masked_where(total1>1.69897000434,total1)
for i in range(7):
	for j in range(6):
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

plt.xticks(np.arange(7),('','1.9-2.0','2.0-2.1','2.1-2.2','2.2-2.3','2.3-2.4','2.4-2.5'), rotation=80)
plt.yticks(np.arange(8),('','D-C2','C2-SLAQ','SLAQ-C3','C3-LRG','LRG-C5','C5-C6','C6-D'))
plt.xlabel('Velocity dispertion bins')
plt.ylabel('Colour bins')
plt.title('Number plot for 0.6 < z < 0.7')
#plt.ylim(0,50)
#plt.savefig('selectiontestV20.4_0.5.png')
plt.show()

