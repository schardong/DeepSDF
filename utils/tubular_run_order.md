# Tubular tests script run order

1. Generate the training and test data (```> tubular_gen_spheres.sh```)
2. Train models (```> tubular_train_spheres.sh```)
3. Reconstruct meshes (```> tubular_reconstruct_spheres.sh```)
4. Convert from stanford file format (```.ply -> .off```) to meshlab format (```> tubular_ply_to_off.sh```)
5. Calculate mesh accuracy and completeness (```> tubular_calc_mesh_acc.sh```)
6. Merge the results in a single CSV (```> tubular_build_single_csv.py```)
