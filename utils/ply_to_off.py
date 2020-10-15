#!/usr/bin/env python3
# coding: utf-8

import argparse
import os
from plyfile import PlyData, PlyElement


def read_and_check_ply(path):
    data = PlyData.read(path)
    points = None
    faces = None
    for i, e in enumerate(data.elements):
        if e.name == "vertex":
            points = e.data
        elif "face" in e.name:
            faces = e.data

    if points is None:
        raise AttributeError(f"vertex list does not exists for file {fname}")
    if not len(points):
        raise AttributeError(f"vertex list is empty for file {fname}")

    if faces is None:
        raise AttributeError(f"face list does not exists for file {fname}")
    if not len(points):
        raise AttributeError(f"face list is empty for file {fname}")

    return points, faces


def write_off(path, points, faces):
    with open(path, "w") as fout:
        print("OFF", file=fout)
        print(len(points), len(faces), 0, file=fout)

        for p in points:
            print(p[0], p[1], p[2], file=fout)

        for f in faces:
            v0, v1, v2 = f[0]
            print("3", v0, v1, v2, file=fout)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert PLY files to OFF format."
    )
    parser.add_argument(
        "input", type=str, help="Path to the input PLY file(s)."
    )
    parser.add_argument(
        "output", type=str, help="Path to the output OFF file(s)."
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
            points, faces = read_and_check_ply(os.path.join(args.input, fname))
            ofname = fname[:-4] + ".off"
            write_off(os.path.join(args.output, ofname), points, faces)

    else:
        print(f"[INFO] Processing \"{args.input}\"")
        points, faces = read_and_check_ply(args.input)
        write_off(args.output, points, faces)
