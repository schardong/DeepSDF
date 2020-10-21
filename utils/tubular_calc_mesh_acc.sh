#!/bin/bash


for frac in {10..90..10}
do
    for npts in {1000..10000..1000}
    do
        echo "Processing ACC for spheres with ${frac}% points on surface and ${npts} samples."
        dirname=spheres_${frac}_${npts}
        for f in ${dirname}/*.off
        do
            outname=${f%.*}.txt
            if [ ! -f ${outname} ]
            then
                ./../../mesh-evaluation/bin/evaluate ${f} ref_sphere/sphere.off ${outname}
            else
                echo "File \"${outname}\" exists, continuing."
            fi
        done
    done
done
