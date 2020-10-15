#!/usr/bin/env python
# coding: utf-8

import argparse
import os
import json
import numpy as np


# This is because DeepSDF assumes all objects to be inside the (-1, 1) box
# and not [-1, 1]
SPHERE_RADIUS = 0.99


def sdf_sphere(p, r=SPHERE_RADIUS):
    return np.linalg.norm(p) - np.abs(r)


def spherical_to_euclidean(pts):
    r"""Converts a set of coordinates from spherical to cartesian coordinates.

    Parameters
    ----------
    pts: numpy.array
        List of points in spherical coordinates. Matrix dimension should be
        Nx3, where N is the number of points.

    Returns
    -------
    numpy.array
        A numpy array of size Nx3 with the euclidean coordinates of the input
        points.
    """
    euc_pts = np.zeros_like(pts)
    sin_theta, cos_theta = np.sin(pts[:, 1]), np.cos(pts[:, 1])
    sin_phi, cos_phi = np.sin(pts[:, 2]), np.cos(pts[:, 2])

    for i in range(pts.shape[0]):
        r = pts[i, 0]
        euc_pts[i, 0] = r * sin_theta[i] * cos_phi[i]
        euc_pts[i, 1] = r * sin_theta[i] * sin_phi[i]
        euc_pts[i, 2] = r * cos_theta[i]

    return euc_pts


def gen_sphere_surface(n_points):
    r"""Generates points on the sphere surface.

    Parameters
    ----------
    n_points: integer
        Number of points to create.

    Returns
    -------
    numpy.array
        A numpy array of size n_points x 3 with the euclidean coordinates of
        the generated points.
    """
    radius = np.array([SPHERE_RADIUS] * n_points)
    theta = np.random.rand(n_points) * np.pi
    phi = np.random.rand(n_points) * 2 * np.pi
    sph_pts = np.array([radius, theta, phi]).T
    return spherical_to_euclidean(sph_pts)


def sample_unit_box(n_samples_sphere):
    r"""Samples SDF values on points in a [-1, 1] range in the X, Y and Z axes.

    This function samples `n_samples_sphere` points uniformly at random in a
    [-1, 1] space on 3D axes and calculates their SDF values.

    Parameters
    ----------
    n_samples_sphere: int
        Number of point samples per sphere.

    Returns
    -------
    sdf: dict
        A dict with keys `pos` for SDF values >= 0 and, `neg` for SDF
        values < 0.
    """
    pts = 2 * np.random.rand(n_samples_sphere, 3) - 1
    mat = np.zeros((n_samples_sphere, 7))
    mat[:, 0:3] = pts
    mat[:, 3:6] = np.array([p / np.linalg.norm(p) for p in pts])
    mat[:, 6] = np.array([sdf_sphere(p) for p in pts])

    return {
        "pos": mat[mat[:, -1] >= 0, :],
        "neg": mat[mat[:, -1] < 0, :]
    }


def gen_splits(nobj, test_frac=0.3):
    data = set(np.arange(start=0, stop=nobj, step=1))
    train = np.random.choice(
        a=list(data),
        size=np.floor((1.0 - test_frac) * nobj).astype(np.int),
        replace=False
    )
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
        "--nobjects", "-n",
        dest="nobj",
        help="The number of objects to create",
        default=100,
        type=int
    )
    parser.add_argument(
        "--nsamples", "-s",
        dest="nsamples",
        help="The number of SDF samples per object.",
        default=1000,
        type=int
    )
    parser.add_argument(
        "--fsurfpoints", "-z",
        dest="fsurfpts",
        help="Percentage of points generated on the object surface (SDF = 0).",
        default=50,
        type=int
    )
    parser.add_argument(
        "--output-dir", "-o",
        dest="output_path",
        help="Folder to save the dataset. Will be created if non-existant.",
        default="out",
        type=str
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
        prog="gen_synth_data.py",
        description="Synthetic data generation for tests."
    )

    add_params(arg_parser)
    args = arg_parser.parse_args()

    if not os.path.exists(args.output_path):
        os.makedirs(args.output_path)

    n_surf_pts = np.floor(args.fsurfpts * args.nsamples / 100.0).astype(np.int)
    n_unif_pts = args.nsamples - n_surf_pts

    for i in range(args.nobj):
        sdf = sample_unit_box(n_unif_pts)
        pts_surf = gen_sphere_surface(n_surf_pts)
        pts_surf = np.hstack((pts_surf, pts_surf, np.zeros((n_surf_pts, 1))))
        sdf["pos"] = np.vstack((sdf["pos"], pts_surf))

        with open(f"{args.output_path}/{i}.npz", "wb") as f:
            np.savez(f, pos=sdf["pos"], neg=sdf["neg"])

    if args.gen_splits:
        gen_splits(args.nobj)
