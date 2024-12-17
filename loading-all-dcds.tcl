mol new step5_input.psf

for {set i 37} {$i < 48} {incr i} {
    mol addfile $i/rest2.job0.$i.dcd 
    mol addfile $i/rest2.job1.$i.dcd
}