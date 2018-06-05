# DeepSeg3D
Neural network toolkit for 3D image segmentation


# Configuration
Copy config.txt and change the value to work on your .

* train_size : number of image to use for training
* train_gd_path  : path for ground truth image
* train_mra_path : path for input image 

* valid_size : number of image to use for validation
* valid_gd_path  : path for ground truth image
* valid_mra_path : path for input image

* test_size : number of image to use for test
* test_gd_path  : path for ground truth image
* test_mra_path : path for input image

* image_size_x : image size (x axis)
* image_size_y : image size (y axis)
* image_size_z : image size (z axis)

* patch_size_x : patch size (x axis)
* patch_size_y : patch size (y axis)
* patch_size_z : patch size (z axis)

* batch_size : size of batch
* steps_per_epoch : steps per epoch
* epochs : number of epochs

* folder = path for logs (logs folder is used for tensorboard logs, training logs and saved models)


# Training
To run the training, launch [training.py](training.py) with python3.

* Limit GPU usage
CUDA_VISIBLE_DEVICES=0,1,2,...

* Use CPU only
CUDA_VISIBLE_DEVICES=''

* Example of training
```
CUDA_VISIBLE_DEVICES=0,1 nohup python3 training.py ./config.txt &
```


# Testing
To run the testing, launch [testing.py](testing.py) with python3.

* Example of test
```
CUDA_VISIBLE_DEVICES=2,3 python3 testing.py ./config.txt ./logs/model-001.h5
```


# Miscellaneous

* remove 90% of saved models in logs folders
```
rm ./logs*/model-[0-9][0-9][1-9]*
```