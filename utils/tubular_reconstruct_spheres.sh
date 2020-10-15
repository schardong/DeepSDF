#!/bin/bash

for frac in {10..90..10}
do
    for npts in {1000..10000..1000}
    do
        echo "Fraction of points on Surface: ${frac}"
        echo "# of points sampled ${npts}"
        python reconstruct.py -e examples/spheres_${frac}_${npts} --split examples/splits/spheres_train_${frac}_${npts}.json -d data/
    done
done
