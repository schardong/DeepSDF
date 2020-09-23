#!/usr/bin/env python3
# Copyright 2004-present Facebook. All Rights Reserved.

import ctypes
import deep_sdf.data
import sys
sys.path.append('../pangolin/build/src')

import OpenGL.GL as gl
import pypangolin as pango

if __name__ == "__main__":

    npz_filename = sys.argv[1]

    data = deep_sdf.data.read_sdf_samples_into_ram(npz_filename)

    xyz_neg = data[1][:, 0:3].numpy().astype(ctypes.c_float)
    xyz_pos = data[0][:, 0:3].numpy().astype(ctypes.c_float)

    win = pango.CreateWindowAndBind("Samples | " + npz_filename, 800, 600)
    gl.glEnable(gl.GL_DEPTH_TEST)

    pm = pango.ProjectionMatrix(800, 600, 420, 420, 400, 300, 0.1, 1000)
    mv = pango.ModelViewLookAt(-0, 0.5, -3, 0, 0, 0, pango.AxisY)
    s_cam = pango.OpenGlRenderState(pm, mv)

    handler = pango.Handler3D(s_cam)
    d_cam = (
        pango.CreateDisplay()
        .SetBounds(
            pango.Attach(0),
            pango.Attach(1),
            pango.Attach(0),
            pango.Attach(1),
            -800.0 / 600.0,
        )
        .SetHandler(handler)
    )

    pango.CreatePanel("ui").SetBounds(
        pango.Attach(0), pango.Attach(1), pango.Attach(0), pango.Attach(0)
    )

    gl.glClearColor(1, 1, 1, 0)

    while not pango.ShouldQuit():

        gl.glClear(gl.GL_COLOR_BUFFER_BIT + gl.GL_DEPTH_BUFFER_BIT)
        d_cam.Activate(s_cam)

        gl.glEnableClientState(gl.GL_VERTEX_ARRAY)

        gl.glColor3ub(0, 0, 0)

        gl.glVertexPointer(
            3, gl.GL_FLOAT, 0, xyz_neg.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
        )

        gl.glDrawArrays(gl.GL_POINTS, 0, xyz_neg.shape[0])

        gl.glDisableClientState(gl.GL_VERTEX_ARRAY)

        pango.FinishFrame()
