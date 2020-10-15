#!/usr/bin/env python
# coding: utf-8

import argparse
import os
from plyfile import PlyData, PlyElement


def write_txt(filepath, points):
    """
    Write a point cloud to txt file in the following format:

        num_points
        point1x point1y point1z
        point2x point2y point2z
        ...

    :param filepath: path to file to read
    :type filepath: str
    :param points: points
    :type points: numpy.ndarray
    """
    with open(filepath, 'w') as f:
        print(str(points.shape[0]), file=f)
        for i in range(points.shape[0]):
            print(f"{str(points[i][0])} {str(points[i][1])} {str(points[i][2])}", file=f)


def read_and_check_ply(fname):
    data = PlyData.read(fname)
    points = None
    for i, e in enumerate(data.elements):
        if e.name == "vertex":
            points = e.data
            break

    if points is None:
        raise AttributeError(f"vertex list does not exists for file {fname}")
    if not len(points):
        raise AttributeError(f"vertex list is empty for file {fname}")

    return points


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert PLY files to TXT format."
    )
    parser.add_argument(
        "input", type=str, help="Path to the input PLY file(s)."
    )
    parser.add_argument(
        "output", type=str, help="Path to the output TXT file(s)."
    )
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print("Input path does not exist. Aborting.")
        exit(1)

    batch = os.path.isdir(args.input)

    if batch and not os.path.exists(args.output):
        dirname = args.output if os.path.isdir(args.output) else os.path.dirname(args.output)
        os.makedirs(dirname)
        print(f"[INFO] Created the \"{dirname}\" directory")

    if batch:
        print(f"[INFO] Processing all files in \"{args.input}\"")
        for fname in os.listdir(args.input):
            print(f"[INFO] Processing \"{fname}\"")
            points = read_and_check_ply(os.path.join(args.input, fname))
            ofname = fname[:-4] + ".txt"
            write_txt(os.path.join(args.output, ofname), points)

    else:
        print(f"[INFO] Processing \"{args.input}\"")
        points = read_and_check_ply(args.input)
        write_txt(args.output, points)
