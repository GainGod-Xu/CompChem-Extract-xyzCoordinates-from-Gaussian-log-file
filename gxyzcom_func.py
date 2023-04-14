#!/usr/bin/python
# -*- coding: utf-8 -*-

import os,math,sys

## Please tell me your jobtype
def gwxyzcom(ifs_name):
    jobtype = input("please input the number of your job type(1.TS 2.opt 3.freq 4.scan 5.irc 6.sp) with \"  \" \n")

    if jobtype == 1:
         com_name=ifs_name[:-4]+'_TS.com'
         chk_name=ifs_name[:-4]+'_TS.chk'

    elif jobtype == 2:
         com_name=ifs_name[:-4]+'_opt.com'
         chk_name=ifs_name[:-4]+'_opt.chk'

    elif jobtype == 3:
         com_name=ifs_name[:-4]+'_freq.com'
         chk_name=ifs_name[:-4]+'_freq.chk'

    elif jobtype == 4:
         com_name=ifs_name[:-4]+'_scan.com'
         chk_name=ifs_name[:-4]+'_scan.chk'

    elif jobtype == 5:
         com_name=ifs_name[:-4]+'_irc.com'
         chk_name=ifs_name[:-4]+'_irc.chk'

    elif jobtype == 6:
         sp_bs=input('Please type the basis set for single point energy! \n')
         com_name=ifs_name[:-4]+ '_' + str(sp_bs) + '_sp.com'
         chk_name=ifs_name[:-4]+ '_' + str(sp_bs) + '_sp.chk'

    else:
         pass
 
    ifs = open(ifs_name,'r')
    xyz_cor=[]
    for line in ifs.readlines()[2:]:
        xyz_cor.append(line)
    ifs.close()
 
    com = open(com_name,'w')
    com.write('%mem=32gb \n')
    com.write('%nprocshared=16 \n')
    com.write('%chk=' + chk_name + '\n')

    if jobtype == 1:
       com.write('#p b3lyp/gen opt=(calcfc,ts,noeigentest) \n')
    elif jobtype == 2:
       com.write('#p b3lyp/gen opt \n')
    elif jobtype == 3:
       com.write('#p b3lyp/gen freq \n')
    elif jobtype == 4:
       com.write('#p b3lyp/gen fopt=(modredundant,maxcycle=15) \n')
    elif jobtype == 5:
       com.write('#p b3lyp/gen irc=(calcfc,MaxPoints=20,stepsize=10) nosym scf(converg=5)  \n')
    elif jobtype == 6:
       com.write('#p b3lyp sp ' + str(sp_bs) +' \n')
    else:
       pass
    com.write('\n')
    com.write('comment  \n')
    com.write('\n')
    com.write('0 2 \n')

    for line in xyz_cor:
        com.write(str(line))

    com.write('\n')

### your gen basis set
    com.write('C N Cl Na O H 0\n')
    com.write('6-311G*\n')
    com.write('****\n')
    com.write('Co 0\n')
    com.write('def2svp\n')
    com.write('****\n')

### write an space line
    com.write('\n')
    com.close()

