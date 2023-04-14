#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import os,math,sys
#
filename= sys.argv[1]
ofs_name=filename[:-4]+'.xyz'

ifs = open(filename, 'r')

while 1:
      line=ifs.readline()
      if not line: break
      data=line.split()
      if len(data)>0: # if true, line is not blank
         if data[0]=='Input' or data[0]=='Standard' or data[0]=='Z-Matrix':
            if data[1]=='orientation:': # Found Standard Orientation
              frame=[]
              line=ifs.readline()  # skip header lines
              line=ifs.readline()  # skip header lines
              line=ifs.readline()  # skip header lines
              line=ifs.readline()  # skip header lines
              line=ifs.readline()  # first line containing atom info
              data=line.split()
              while data[0] != '---------------------------------------------------------------------':
                  
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
                      print (data,'no atom type found, exiting....')
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
                     print ('cannot work out Standard orientation format. exiting..')
                     break 
                  ### create a format for your atom information by using a list
                  atominfo=[atomid,atomtype,atomx,atomy,atomz]
                  #print atominfo   
                  ### store your atom information into frame
                  frame.append(atominfo)
                  ##read  
                  line=ifs.readline()
                  data=line.split()


ofs = open(ofs_name, 'w')
ofs.write(str(len(frame)) + '\n\n')
for i in frame:
    ofs.write(i[1] + ' ' +  '%15.8f' % float(i[2]) + ' ' + '%15.8f' % float(i[3]) + ' ' + '%15.8f' % float(i[4]) + '\n')

ifs.close()
ofs.close()

