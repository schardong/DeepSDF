#!/usr/bin/env python
# coding: utf-8


import argparse
import os
import numpy as np
import pandas as pd


def extract_mesh_perc_npoints(fname):
    """Extracts the mesh type, percentage of points on the surface and, number
    of points in the mesh from the filename.

    Parameters
    ----------
    fname: str
        The filename following the format: 'meshtype_perc_npoints/filename.extension'

    Returns
    -------
    mesh: str
        The mesh type: First part of the dirname
    perc: int
        Percentage of points in the mesh surface (second part of the dirname)
    npoints: int
        Total number of samples in the mesh (last part of the dirname)

    Raises
    ------
    ValueError
        If one of the fields is missing, i.e. splitting the dirname should
        yield a list with three elements at least.

    TypeError
        If either the percentage or the number of points is not convertible
        to integer.

    Examples
    --------
    >>> extract_mesh_perc_npoints(spheres_10_1000/0.off)
    >>> ('spheres', 10, 1000)
    """
    dirname = os.path.dirname(fname).split("_")
    if len(dirname) < 2:
        raise ValueError("Not enough values in pathname")

    try:
        mesh, perc, npoints = dirname[0], int(dirname[-2]), int(dirname[-1])
    except TypeError:
        print("Could not convert fields to int. Returning 0.")
        return None, 0, 0
    else:
        return mesh, perc, npoints


def read_txt(path):
    with open(path, "r") as fin:
        lines = fin.readlines()
        lines = [l.strip() for l in lines if l.strip() != ""]

        fline = lines[0].split(" ")
        _, acc, comp = fline

    return acc, comp


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""
        Merge the accuracy and completeness measures from all
        experiments in a CSV file.
        """
    )
    parser.add_argument(
        "input", type=str, nargs="+", help="Input TXT files."
    )
    parser.add_argument(
        "output", type=str, default="out.csv", help="Path to the output CSV file."
    )
    parser.add_argument(
        "--skip", "-s", action="store_true", default=False,
        help="Skips processing the directory if the output file exists."
    )
    args = parser.parse_args()

    if args.skip and os.path.exists(args.output):
        print("[INFO] Output file exists. Skipping.")

    mat = np.zeros((len(args.input), 5))
    for i, fname in enumerate(args.input):
        print(f"[INFO] Processing \"{fname}\"")

        if not os.path.exists(fname):
            print(f"[INFO] File \"{fname}\" does not exists, continuing.")
            continue

        acc, comp = read_txt(fname)
        _, perc, npoints = extract_mesh_perc_npoints(fname)
        scen = int(fname.split("/")[-1][:-4])
        mat[i, :] = [perc, npoints, scen, acc, comp]

    cols = ("percentage", "num_points", "scenario", "accuracy", "completeness")
    df = pd.DataFrame(columns=cols, data=mat)
    df.to_csv(args.output, index=False)
