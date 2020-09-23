#!/bin/bash

python3 preprocess_data.py --data_dir data --source /mnt/old-home/gschardong/projects/ShapeNetCore.v2/ --name ShapeNetV2 --split examples/splits/sv2_chairs_train.json --threads 10 --skip
python3 preprocess_data.py --data_dir data --source /mnt/old-home/gschardong/projects/ShapeNetCore.v2/ --name ShapeNetV2 --split examples/splits/sv2_lamps_train.json --threads 10 --skip
python3 preprocess_data.py --data_dir data --source /mnt/old-home/gschardong/projects/ShapeNetCore.v2/ --name ShapeNetV2 --split examples/splits/sv2_planes_train.json --threads 10 --skip
python3 preprocess_data.py --data_dir data --source /mnt/old-home/gschardong/projects/ShapeNetCore.v2/ --name ShapeNetV2 --split examples/splits/sv2_sofas_train.json --threads 10 --skip
python3 preprocess_data.py --data_dir data --source /mnt/old-home/gschardong/projects/ShapeNetCore.v2/ --name ShapeNetV2 --split examples/splits/sv2_tables_train.json --threads 10 --skip

python3 preprocess_data.py --data_dir data --source /mnt/old-home/gschardong/projects/ShapeNetCore.v2/ --name ShapeNetV2 --split examples/splits/sv2_chairs_test.json --threads 10 --skip --test
python3 preprocess_data.py --data_dir data --source /mnt/old-home/gschardong/projects/ShapeNetCore.v2/ --name ShapeNetV2 --split examples/splits/sv2_lamps_test.json --threads 10 --skip --test
python3 preprocess_data.py --data_dir data --source /mnt/old-home/gschardong/projects/ShapeNetCore.v2/ --name ShapeNetV2 --split examples/splits/sv2_planes_test.json --threads 10 --skip --test
python3 preprocess_data.py --data_dir data --source /mnt/old-home/gschardong/projects/ShapeNetCore.v2/ --name ShapeNetV2 --split examples/splits/sv2_sofas_test.json --threads 10 --skip --test
python3 preprocess_data.py --data_dir data --source /mnt/old-home/gschardong/projects/ShapeNetCore.v2/ --name ShapeNetV2 --split examples/splits/sv2_tables_test.json --threads 10 --skip --test

python3 preprocess_data.py --data_dir data --source /mnt/old-home/gschardong/projects/ShapeNetCore.v2/ --name ShapeNetV2 --split examples/splits/sv2_chairs_test.json --threads 10 --skip --surface
python3 preprocess_data.py --data_dir data --source /mnt/old-home/gschardong/projects/ShapeNetCore.v2/ --name ShapeNetV2 --split examples/splits/sv2_lamps_test.json --threads 10 --skip --surface
python3 preprocess_data.py --data_dir data --source /mnt/old-home/gschardong/projects/ShapeNetCore.v2/ --name ShapeNetV2 --split examples/splits/sv2_planes_test.json --threads 10 --skip --surface
python3 preprocess_data.py --data_dir data --source /mnt/old-home/gschardong/projects/ShapeNetCore.v2/ --name ShapeNetV2 --split examples/splits/sv2_sofas_test.json --threads 10 --skip --surface
python3 preprocess_data.py --data_dir data --source /mnt/old-home/gschardong/projects/ShapeNetCore.v2/ --name ShapeNetV2 --split examples/splits/sv2_tables_test.json --threads 10 --skip --surface
