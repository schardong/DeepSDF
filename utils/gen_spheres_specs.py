#!/usr/bin/env python3
# coding: utf-8

import os
import json


SURF_PERCS = [10, 20, 30, 40, 50, 60, 70, 80, 90]
N_POINTS = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

with open("specs.json", "r") as fin:
    spec = json.load(fin)

for p in SURF_PERCS:
    for n in N_POINTS:
        if not os.path.exists(f"examples/spheres_{p}_{n}"):
            os.makedirs(f"examples/spheres_{p}_{n}")

        spec["TrainSplit"] = f"examples/splits/spheres_train_{p}_{n}.json"

        with open(f"examples/spheres_{p}_{n}/specs.json", "w") as fout:
            print(
                json.dumps(spec,
                           sort_keys=True,
                           ensure_ascii=True,
                           indent=4),
                file=fout
            )
