#!/bin/bash

python preprocess_data.py --data_dir data --source ~/projects/ShapeNetCore.v2/ --name ShapeNetV2 --split examples/splits/sv2_chairs_train.json --threads 6 --skip
python preprocess_data.py --data_dir data --source ~/projects/ShapeNetCore.v2/ --name ShapeNetV2 --split examples/splits/sv2_lamps_train.json --threads 6 --skip
python preprocess_data.py --data_dir data --source ~/projects/ShapeNetCore.v2/ --name ShapeNetV2 --split examples/splits/sv2_planes_train.json --threads 6 --skip
python preprocess_data.py --data_dir data --source ~/projects/ShapeNetCore.v2/ --name ShapeNetV2 --split examples/splits/sv2_sofas_train.json --threads 6 --skip
python preprocess_data.py --data_dir data --source ~/projects/ShapeNetCore.v2/ --name ShapeNetV2 --split examples/splits/sv2_tables_train.json --threads 6 --skip

python preprocess_data.py --data_dir data --source ~/projects/ShapeNetCore.v2/ --name ShapeNetV2 --split examples/splits/sv2_chairs_test.json --threads 6 --skip --test
python preprocess_data.py --data_dir data --source ~/projects/ShapeNetCore.v2/ --name ShapeNetV2 --split examples/splits/sv2_lamps_test.json --threads 6 --skip --test
python preprocess_data.py --data_dir data --source ~/projects/ShapeNetCore.v2/ --name ShapeNetV2 --split examples/splits/sv2_planes_test.json --threads 6 --skip --test
python preprocess_data.py --data_dir data --source ~/projects/ShapeNetCore.v2/ --name ShapeNetV2 --split examples/splits/sv2_sofas_test.json --threads 6 --skip --test
python preprocess_data.py --data_dir data --source ~/projects/ShapeNetCore.v2/ --name ShapeNetV2 --split examples/splits/sv2_tables_test.json --threads 6 --skip --test

python preprocess_data.py --data_dir data --source ~/projects/ShapeNetCore.v2/ --name ShapeNetV2 --split examples/splits/sv2_chairs_test.json --threads 6 --skip --surface
python preprocess_data.py --data_dir data --source ~/projects/ShapeNetCore.v2/ --name ShapeNetV2 --split examples/splits/sv2_lamps_test.json --threads 6 --skip --surface
python preprocess_data.py --data_dir data --source ~/projects/ShapeNetCore.v2/ --name ShapeNetV2 --split examples/splits/sv2_planes_test.json --threads 6 --skip --surface
python preprocess_data.py --data_dir data --source ~/projects/ShapeNetCore.v2/ --name ShapeNetV2 --split examples/splits/sv2_sofas_test.json --threads 6 --skip --surface
python preprocess_data.py --data_dir data --source ~/projects/ShapeNetCore.v2/ --name ShapeNetV2 --split examples/splits/sv2_tables_test.json --threads 6 --skip --surface
