# CompChem-Extract-xyzCoordinates-from-Gaussian-log-file
1. Make the python scripts excutable:  
chmod +x *.py 

2. The usage of python scripts:
1) Read xyz and optization/TS searching parameters from calculation:   
read_xyz_parameters.py molecule_A.log  

2) Read xyz and energy from scan calculation to visualize the potential energy change, you can extract particular one structure or all of them:   
read_xyz_energy_from_scan.py scan.log  

3) Read xyz and energy from irc calculation to visualize the reaction pathway, you can extract particular one structure or all of them:     
read_xyz_parameters.py irc.log    


