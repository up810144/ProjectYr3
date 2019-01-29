
#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -o /users/zt810144/junk/z_run.o.${PBS_JOBID}
#PBS -e /users/zt810144/junk/z_run.e.${PBS_JOBID}
#PBS -q sciama3.q
#PBS -M up810144@myport.ac.uk
module purge
module add apps/anaconda3/2.5.0
path='/users/zt810144/project/'

prog='zak.py'

runp=$path$prog

echo $runp
time python $runp


