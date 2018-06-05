# ------------------------------------------------------------ #
#
# file : utils/config/read.py
# author : CM
# Read the configuration
#
# ------------------------------------------------------------ #

import configparser

def readConfig(filename):

    # ----- Read the configuration ----
    config = configparser.RawConfigParser()
    config.read_file(open(filename))

    dataset_train_size      = int(config.get("dataset","train_size"))
    dataset_train_gd_path   = config.get("dataset","train_gd_path")
    dataset_train_mra_path  = config.get("dataset","train_mra_path")

    dataset_valid_size      = int(config.get("dataset","valid_size"))
    dataset_valid_gd_path   = config.get("dataset","valid_gd_path")
    dataset_valid_mra_path  = config.get("dataset","valid_mra_path")

    dataset_test_size       = int(config.get("dataset","test_size"))
    dataset_test_gd_path    = config.get("dataset","test_gd_path")
    dataset_test_mra_path   = config.get("dataset","test_mra_path")

    image_size_x = int(config.get("data","image_size_x"))
    image_size_y = int(config.get("data","image_size_y"))
    image_size_z = int(config.get("data","image_size_z"))

    patch_size_x = int(config.get("patchs","patch_size_x"))
    patch_size_y = int(config.get("patchs","patch_size_y"))
    patch_size_z = int(config.get("patchs","patch_size_z"))

    batch_size      = int(config.get("train","batch_size"))
    steps_per_epoch = int(config.get("train","steps_per_epoch"))
    epochs          = int(config.get("train","epochs"))

    logs_folder     = config.get("logs","folder")

    return {"dataset_train_size"    : dataset_train_size,
            "dataset_train_gd_path" : dataset_train_gd_path,
            "dataset_train_mra_path": dataset_train_mra_path,
            "dataset_valid_size"    : dataset_valid_size,
            "dataset_valid_gd_path" : dataset_valid_gd_path,
            "dataset_valid_mra_path": dataset_valid_mra_path,
            "dataset_test_size"     : dataset_test_size,
            "dataset_test_gd_path"  : dataset_test_gd_path,
            "dataset_test_mra_path" : dataset_test_mra_path,
            "image_size_x" : image_size_x,
            "image_size_y" : image_size_y,
            "image_size_z" : image_size_z,
            "patch_size_x" : patch_size_x,
            "patch_size_y" : patch_size_y,
            "patch_size_z" : patch_size_z,
            "batch_size" : batch_size,
            "steps_per_epoch" : steps_per_epoch,
            "epochs" : epochs,
            "logs_folder" : logs_folder
            }