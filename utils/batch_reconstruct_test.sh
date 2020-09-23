#!/bin/bash

#SOFAS
python reconstruct.py -e examples/sofas/ -c 100 -d data -s examples/splits/sv2_sofas_test.json --skip
python reconstruct.py -e examples/sofas/ -c 500 -d data -s examples/splits/sv2_sofas_test.json --skip
python reconstruct.py -e examples/sofas/ -c 1000 -d data -s examples/splits/sv2_sofas_test.json --skip
python reconstruct.py -e examples/sofas/ -c 2000 -d data -s examples/splits/sv2_sofas_test.json --skip

#PLANES
python reconstruct.py -e examples/planes/ -c 100 -d data -s examples/splits/sv2_planes_test.json --skip
python reconstruct.py -e examples/planes/ -c 500 -d data -s examples/splits/sv2_planes_test.json --skip
python reconstruct.py -e examples/planes/ -c 1000 -d data -s examples/splits/sv2_planes_test.json --skip
python reconstruct.py -e examples/planes/ -c 2000 -d data -s examples/splits/sv2_planes_test.json --skip

#LAMPS
python reconstruct.py -e examples/lamps/ -c 100 -d data -s examples/splits/sv2_lamps_test.json --skip
python reconstruct.py -e examples/lamps/ -c 500 -d data -s examples/splits/sv2_lamps_test.json --skip
python reconstruct.py -e examples/lamps/ -c 1000 -d data -s examples/splits/sv2_lamps_test.json --skip
python reconstruct.py -e examples/lamps/ -c 2000 -d data -s examples/splits/sv2_lamps_test.json --skip
