#!/bin/bash


for frac in {10..90..10}
do
    for npts in {1000..10000..1000}
    do
        dirname=spheres_${frac}_${npts}
        echo "Converting from PLY to OFF for ${frac}% points and ${npts} samples."
        python ply_to_off.py --skip ../examples/${dirname}/Reconstructions/100/Meshes/simple/${dirname}/ spheres_${frac}_${npts}/
    done
done
