set num_frames [molinfo top get numframes]
set outfolder "hole-analysis/37-47rep"
for {set frame 0} {$frame < $num_frames} {incr frame 100} {
    # Set the current frame
    animate goto $frame
    set prot [atomselect top "protein"]
    file mkdir $outfolder/$frame/
    $prot writepdb $outfolder/$frame/$frame.pdb
    
    $prot delete

}