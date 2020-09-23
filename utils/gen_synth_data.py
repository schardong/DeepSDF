#!/usr/bin/env python
# coding: utf-8

import argparse
import os
import json
import numpy as np


def sdf_sphere(p, r=1):
    return np.linalg.norm(p) - np.abs(r)


def gen_data(nobj, nsamples):
    if not os.path.exists("spheres"):
        os.makedirs("spheres")
    for i in range(nobj):
        pts = 2 * np.random.rand(nsamples, 3) - 1
        mat = np.zeros((nsamples, 7))
        mat[:, 0:3] = pts
        mat[:, 3:6] = np.array([p / np.linalg.norm(p) for p in pts])
        mat[:, 6] = np.array([sdf_sphere(p) for p in pts])

        samples = {
            "pos": mat[mat[:, -1] >= 0, :],
            "neg": mat[mat[:, -1] < 0, :]
        }

        with open(f"spheres/{i}.npz", "wb") as f:
            np.savez(f, pos=samples["pos"], neg=samples["neg"])


def gen_splits(nobj, test_frac=0.7):
    data = set(np.arange(start=0, stop=nobj, step=1))
    train = np.random.choice(a=list(data), size=np.floor(0.7 * nobj).astype(np.int), replace=False)
    test = data - set(train)

    train = sorted(train)
    train_fnames = [None] * len(train)
    for i, t in enumerate(train):
        train_fnames[i] = f"{t}"

    test = sorted(list(test))
    test_fnames = [None] * len(test)
    for i, t in enumerate(test):
        test_fnames[i] = f"{t}"

    with open('spheres_train.json', 'w') as f:
        data = {
            "simple": {
                "spheres": train_fnames
            }
        }
        print(json.dumps(data, sort_keys=True, ensure_ascii=False, indent=4), file=f)

    with open('spheres_test.json', 'w') as f:
        data = {
            "simple": {
                "spheres": test_fnames
            }
        }
        print(json.dumps(data, sort_keys=True, ensure_ascii=False, indent=4), file=f)


def add_params(parser):
    parser.add_argument(
        "--nobjects", "-o",
        dest="nobj",
        help="The nember of objects to create",
        default=1000,
        type=int
    )
    parser.add_argument(
        "--nsamples", "-s",
        dest="nsamples",
        help="The number of SDF samples per object.",
        default=10000,
        type=int
    )
    parser.add_argument(
        "--gen_splits", "-g",
        dest="gen_splits",
        help="Generates a new set of train/test splits.",
        action="store_true",
        default=False
    )


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(
        prog="gen_data.py",
        description="Sythetic data generation for tests."
    )

    add_params(arg_parser)
    args = arg_parser.parse_args()
    gen_data(args.nobj, args.nsamples)

    if args.gen_splits:
        gen_splits(args.nobj)
