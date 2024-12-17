### Usage - 
1. Load the dcd files into vmd using loading-all-dcds.tcl
2. save the pdb frames with saving-frames.tcl (the increament can be changed as wished)
3. run hole program using running-highthroughput-hole.sh in all the saved frames. Make sure to have 'simple.rad' file in the working directory as specified.
4. After running hole program use extracting-hole-data.sh to extract the coordinates and pore radius.
5. use plotting-hole-data.py to get a 3D interactive plot. (Plotly must be in the environment)
   
