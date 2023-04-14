#!/usr/bin/python

# -*- coding: iso-8859-15 -*-


import os,math,sys,time
from gxyz_hao import readxyz
from gxyz_hao import ext_exact
from gxyzcom_func import gwxyzcom

#import numpy as np
#import matplotlib.pyplot as plt
#

def ext_energy():
    ifs = open(input_file, 'r')
    scan_dist=[]
    SCF=0.0 # initiate
    energies=[]
    all_energies=[]
    step_number=[]
    frames_opt=[]
    i=-1
#    lines=ifs.readline()
#    for line in lines:
#        data=line.split()
#        if len(data)>4: # if true, line is not blank
#           if data[4]=='Scan': # define scan variable
#              bond_ids=data[2]
    while 1:
          line=ifs.readline()
          if not line: break
          data=line.split()
          if len(data)>4: # if true, line is not blank
             if data[4]=='Scan':
                bond_ids=data[2]
 #               print (str(bond_ids))
                break # stop reading file..
          

    for line in ifs.readlines():
        data=line.split()
        if len(data)>4: # if true, line is not blank
           if data[2]==bond_ids and not data[4]=='Scan': 
              scan_dist.append(float(data[3]))      
           if data[0]=='SCF' and data[1]=='Done:': 
              SCF=float(data[4])
              all_energies.append(SCF)
           if data[0] == 'Step' and data[1] == 'number' and data[3] =='out':
                 step_number.append(data[12])
                 #i+=1
                 if i >=1:
                    if int(step_number[i]) ==(int(step_number[i-1]) + 1) :  
                       energies.append(all_energies[i-1])
                       frames_opt.append(frames[i-1])   
                       print(i)
                 i+=1 
    energies.append(all_energies[i])
    frames_opt.append(frames[i])

    k=0
    l=1
    if len(energies) > len(scan_dist):
       last_dist= 2*scan_dist[len(scan_dist)-1]-scan_dist[len(scan_dist)-2]
       scan_dist.append(last_dist)
             
    print('Spots'+'   '+ 'Bond Distance' +'   ' + 'Relative Energy'+ '     ' + 'Absolute Energy'    + '' )
    for i in energies:
        print('%3s' % str(l) + '      '+'%3.2f' % float(scan_dist[k]) + '              ' + '%3.1f' % float(627.51*(i-energies[0]))  + '              ' +'%10.10f' % float(energies[k]) + '' )
        k+=1
        l+=1
    ifs.close()
    return scan_dist, energies, frames_opt

def write_scan_energy(scan_dist, energies):
    out_file = input_file[:-4]+'.scan_energy' # your output file
    ofs = open(out_file, 'w')
    k=0
    l=1
    for i in energies:
        ofs.write('%3s' % str(l) + '      ' + '%4.2f' % float(scan_dist[k]) + '                       ' + '%3.1f' % float(627.51*(i-energies[0])) +'                        '+ '%10.10f' % float(energies[k]) + '\n' )

        k+=1
        l+=1
    ofs.close()

def pr_energy(scan_dist,energies):
    delta_E=[]
    for i in energies:
        delta_E.append(float(627.51*(i-energies[0])))
    out_file = input_file[:-4]+'_BE.png'
    plt.figure('Draw')
    plt.plot(scan_dist,delta_E)
    plt.draw()
    plt.pause(5)
    plt.savefig(out_file)
    plt.close()

####Entry: main function#######
if __name__ == "__main__":
   input_file = sys.argv[1] # It is your scan .log file
   frames=readxyz(input_file)
   x,y,z=ext_energy()
   write_scan_energy(x,y)
#   pr_energy(x,y)
   print('*****************************************************************************')
   print('The lenth of frames is ' + str(len(z)))
   job_type = int(input('if you want ts xyz file, please type 1 (for only 1 frame)or 100(for all frames); otherwise, type 0\n')) 
   print('*****************************************************************************\n\n\n')
   if job_type:
      n = int(input('which frame do you want on there?\n')) -1
      xyz_file = ext_exact(input_file,z,n)
      gwxyzcom(xyz_file)
   else:
      pass



