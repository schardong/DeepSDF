#!/bin/bash

for frac in {10..90..10}
do
    for npts in {1000..10000..1000}
    do
        echo "Generating spheres with for ${frac}% points on surface."
        echo "Generating spheres with ${npts} samples."
        python3 gen_synth_data.py -n 100 -s ${npts} -z ${frac} -o spheres_${frac}_${npts}
    done
done
