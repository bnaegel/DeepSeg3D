# ------------------------------------------------------------ #
#
# file : training.py
# author : CM
# Launch the training
#
# ------------------------------------------------------------ #
import os
import sys
import numpy as np
from utils.config.read import readConfig
from utils.io.read import readDataset, reshapeDataset
from utils.learning.patch.extraction import generatorRandomPatchs
from models.unet import unet_3
from utils.learning.metrics import sensitivity, specificity, precision
from utils.learning.losses import dice_coef, dice_coef_loss, dice_coef_, dice_coef_loss_
from keras.optimizers import Adam
from keras.callbacks import CSVLogger, TensorBoard, ModelCheckpoint, LearningRateScheduler

from keras import backend as K
K.set_image_dim_ordering("tf")

config_filename = sys.argv[1]
if(not os.path.isfile(config_filename)):
    sys.exit(1)

config = readConfig(config_filename)

print("Loading training dataset")

train_gd_dataset = readDataset(config["dataset_train_gd_path"],
                               config["dataset_train_size"],
                               config["image_size_x"],
                               config["image_size_y"],
                               config["image_size_z"])
train_gd_dataset = reshapeDataset(train_gd_dataset)

train_mra_dataset = readDataset(config["dataset_train_mra_path"],
                                config["dataset_train_size"],
                                config["image_size_x"],
                                config["image_size_y"],
                                config["image_size_z"])
train_mra_dataset = reshapeDataset(train_mra_dataset)

print("Generate model")

model = unet_3(config["patch_size_x"],config["patch_size_y"],config["patch_size_z"])
# plot_model(model, to_file='model.png')
# model = multi_gpu_model(model,2)
model.compile(optimizer=Adam(lr=1e-4), loss=dice_coef_loss, metrics=[dice_coef, sensitivity, specificity, precision,
                                                                     dice_coef_, dice_coef_loss_, dice_coef_loss])

print("Start training")

tensorboard = TensorBoard(log_dir=config["logs_folder"], histogram_freq=0, write_graph=True, write_images=True)
csv_logger = CSVLogger(str(config["logs_folder"]+'training.log'))
checkpoint = ModelCheckpoint(filepath=str(config["logs_folder"]+'model-{epoch:03d}.h5'))

def learning_rate_schedule(initial_lr=1e-4, decay_factor=0.99, step_size=1):
    def schedule(epoch):
        x = initial_lr * (decay_factor ** np.floor(epoch / step_size))
        print("Learning rate : ",x)
        return x
    return LearningRateScheduler(schedule)

# lr_sched = learning_rate_schedule(initial_lr=1e-3, decay_factor=0.95, step_size=1)
lr_sched = learning_rate_schedule(initial_lr=1e-4, decay_factor=0.99, step_size=1)


model.fit_generator(generatorRandomPatchs(train_mra_dataset, train_gd_dataset, config["batch_size"],
                                          config["patch_size_x"],config["patch_size_y"],config["patch_size_z"]),
                    steps_per_epoch=config["steps_per_epoch"], epochs=config["epochs"],
                    verbose=1, callbacks=[tensorboard, csv_logger, checkpoint, lr_sched])

model.save(str(config["logs_folder"]+'model-final.h5'))

"""
# Validation
# free dataset memory
train_gd_dataset = None
train_mra_dataset = None

valid_gd_dataset = readDataset(config["dataset_valid_gd_path"],
                               config["dataset_valid_size"],
                               config["image_size_x"],
                               config["image_size_y"],
                               config["image_size_z"])
valid_gd_dataset = reshapeDataset(valid_gd_dataset)

valid_mra_dataset = readDataset(config["dataset_valid_mra_path"],
                                config["dataset_valid_size"],
                                config["image_size_x"],
                                config["image_size_y"],
                                config["image_size_z"])
valid_mra_dataset = reshapeDataset(valid_mra_dataset)
"""