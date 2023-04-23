#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os,math,sys,time
from read_xyz_parameters import ext_exact
from read_xyz_parameters import ext_all
import numpy as np
import matplotlib.pyplot as plt

def readxyz(input_file):
    ifs = open(input_file, 'r')
    frames=[]
    pointNum = []
    while 1:
          line=ifs.readline()
          if not line: break
          data=line.split()
          if len(data)>4: # if true, line is not blank
             if data[3]=='Path' and data[4] == 'Number:':
                pointNum.append(int(data[2])) 
          if len(data) > 0:
             if data[0]=='Input':
                if data[1]=='orientation:': # Found Standard Orientation
                   frame=[]
                   line=ifs.readline()  # skip header lines
                   line=ifs.readline()  # skip header lines
                   line=ifs.readline()  # skip header lines
                   line=ifs.readline()  # skip header lines
                   line=ifs.readline()  # first line containing atom info
                   data=line.split()
                   while data[0]!='---------------------------------------------------------------------':
                         atomid=data[0]
                         if   data[1]=='1':   atomtype='H'
                         elif data[1]=='2':   atomtype='He'
                         elif data[1]=='10':   atomtype='Ne'
                         elif data[1]=='18':   atomtype='Ar'
                         elif data[1]=='6':   atomtype='C'
                         elif data[1]=='8':   atomtype='O'
                         elif data[1]=='7':   atomtype='N'
                         elif data[1]=='17':  atomtype='Cl'
                         elif data[1]=='9':   atomtype='F' 
                         elif data[1]=='14':  atomtype='Si' 
                         elif data[1]=='16':  atomtype='S'
                         elif data[1]=='5' :  atomtype='B'
                         elif data[1]=='15' : atomtype='P'
                         elif data[1]=='35' : atomtype='Br'
                         elif data[1]=='29' : atomtype='Cu'
                         elif data[1]=='44' : atomtype='Ru'
                         elif data[1]=='53' : atomtype='I'
                         elif data[1]=='3' : atomtype='Li'
                         elif data[1]=='42' : atomtype='Mo' 
                         elif data[1]=='30' : atomtype='Zn'
                         elif data[1]=='13' : atomtype='Al'
                         elif data[1]=='11' : atomtype='Na'
                         elif data[1]=='19' : atomtype='K'
                         elif data[1]=='74' : atomtype='W'
                         elif data[1]=='47' : atomtype='Ag'
                         elif data[1]=='26' : atomtype='Fe'
                         elif data[1]=='45' : atomtype='Rh'
                         elif data[1]=='46' : atomtype='Pd'
                         elif data[1]=='78' : atomtype='Pt'
                         elif data[1]=='77' : atomtype='Ir'
                         elif data[1]=='27' : atomtype='Co'
                         elif data[1]=='37' : atomtype='Rb'
                         elif data[1]=='40' : atomtype='Zr'
                         elif data[1]=='28' : atomtype='Ni'
                         elif data[1]=='55' : atomtype='Cs'
                         elif data[1]=='34' : atomtype='Se'
                         elif data[1]=='12' : atomtype='Mg'
                         else: 
                              print ('data, no atom type found, exiting....')
                              exit
                  
                         if len(data)==6: 
                            atomx=data[3]
                            atomy=data[4]
                            atomz=data[5]
                         elif len(data)==5:
                            atomx=data[2]
                            atomy=data[3]
                            atomz=data[4] 
                         else: 
                            print('cannot work out Standard orientation format. exiting..')
                            break 
                         ### create a format for your atom information by using a list
                         atominfo=[atomid,atomtype,atomx,atomy,atomz]
                         #print atominfo   
                         ### store your atom information into frame
                         frame.append(atominfo)
                         ##read  
                         line=ifs.readline()
                         data=line.split()
                   frames.append(frame)

                   ###remove un-fully-opt frame###  
                   if len(frames) > len(pointNum):
                      frames.pop((len(frames)-2))

             ###reaction path changes#   
             if data[0]=='Beginning' and data[1] == 'calculation' and data[4]=='REVERSE':
                frames.reverse()
    ifs.close()
    return frames
    

def ext_energy():
    ifs = open(input_file, 'r')
    SCF=0.0 # initiate
    energies=[]
    ###new modification##
    pointNum = []    
    ### read SCF Done###
    for line in ifs.readlines():
        data=line.split()
        if len(data)>4: # if true, line is not blank
           if data[3]=='Path' and data[4] == 'Number:':
              pointNum.append(int(data[2]))

           if data[0]=='Beginning' and data[1] == 'calculation' and data[4]=='REVERSE':
              path_len = len(energies)
              energies.reverse()

           if data[0]=='SCF' and data[1]=='Done:':
              SCF=float(data[4])
              energies.append(SCF)
              if len(energies) > len(pointNum):                 
                 energies.pop((len(energies)-2))        
    ifs.close()
    return energies

def write_irc_energy(energies):
    out_file = input_file[:-4]+'.energy' # your output file
    ofs = open(out_file, 'w')
    l=1
    for i in energies:
        ofs.write('%3s' % str(l) + '      ' + '%3.1f' % float(627.51*(i-energies[0])) +'    '+ '%10.10f' % float(energies[l-1]) + '\n' )
        l+=1
    ofs.close()

def write_irc_xyz(frames):
    out_file = input_file[:-4]+'_irc.xyz' # your output file
    ofs = open(out_file, 'w')
    l=1 
    for i in frames:
        ofs.write( str(i) + '\n' )
        l+=1
    ofs.close()

def pr_energy(energies):
    delta_E=[]
    for i in energies:
        delta_E.append(float(627.51*(i-energies[0])))
    out_file = input_file[:-4]+'.png'
    plt.figure('Draw')
    plt.plot(delta_E)
    plt.draw()
    plt.pause(2)
    plt.savefig(out_file)
    plt.close()


####Entry: main function#######
if __name__ == "__main__":
   input_file = sys.argv[1] # It is your scan .log file
   frames=readxyz(input_file)
   x = ext_energy()
   print("energy frames: " + str(len(x)))
   print("xyz frames: " + str(len(frames)))
   
   n_r=input('If you want to reverse the reaction path, please type 1; if not type 0.\n')
   if int(n_r)==1:
      x.reverse()
      frames.reverse()
   else:
      pass
   write_irc_energy(x)
   pr_energy(x)
           
   print('*****************************************************************************')
   if len(x) == (len(frames)):
      print('IRC is complete \n')
   else:
      print('IRC calculation is not finised yet! \n')
   job_type = int(input('if you want xyz files, please type 1; otherwise, type 0\n'))
   print('*****************************************************************************\n\n\n')
   if job_type:
      ext_all(input_file,frames)
      for n in range(len(frames)):
          xyz_file = ext_exact(input_file,frames,n)
          ###gwxyzcom(xyz_file)

   else:
      print('Well Done on there!') 



