#!/bin/bash

python train_deep_sdf.py -e examples/sofas -c latest
python train_deep_sdf.py -e examples/planes -c latest
python train_deep_sdf.py -e examples/lamps -c latest
python train_deep_sdf.py -e examples/tables -c latest
python train_deep_sdf.py -e examples/chairs -c latest
