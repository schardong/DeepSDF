#!/bin/bash

for frac in {10..90..10}
do
    for npts in {1000..10000..1000}
    do
        echo "Fraction of points on Surface: ${frac}"
        echo "# of points sampled ${npts}"
        python train_deep_sdf.py -e examples/spheres_${frac}_${npts}
    done
done
