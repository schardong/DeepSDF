#!/usr/bin/env python3
# coding: utf-8

import json


SURF_PERCS = [10, 20, 30, 40, 50, 60, 70, 80, 90]
N_POINTS = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

with open("examples/splits/spheres_train.json", "r") as fin:
    splits = json.load(fin)
    spheres_fnames = splits["simple"]["spheres"]

for p in SURF_PERCS:
    for n in N_POINTS:
        with open(f"examples/splits/spheres_train_{p}_{n}.json", "w") as fout:
            data = {
                "simple": {
                    f"spheres_{p}_{n}": spheres_fnames
                }
            }
            print(
                json.dumps(data,
                           sort_keys=True,
                           ensure_ascii=True,
                           indent=4),
                file=fout
            )
