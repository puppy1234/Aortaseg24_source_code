# Aortaseg24
Source code for Miccai challenge: Aortaseg24 
Group members: Yuchong Gao, Hongye Zeng, Haoyu Zheng, Rui Zheng

This is a detailed instructions on how to generate the segmentation output using the provided code.
The code of our group was based on nnUnet. Therefore, the installation and data conversion problem can refer to (https://github.com/MIC-DKFZ/nnUNet). The training and inference code were provided in training.py and inference.py. You can change our configuration and try out more methods.
The training data format should follow https://github.com/MIC-DKFZ/nnUNet/blob/master/documentation/dataset_format.md
The inference data format should be https://github.com/MIC-DKFZ/nnUNet/blob/master/documentation/dataset_format_inference.md

# Data Training
In data training phase, we trained 3d_fullres network based on given dataset. Apart from 5-fold cross-validation, we trained the network based on all data. Therefore, in order to train the network, we use:
```python train.py dataset_name 3d_fullres all --npz```
If you want to use 5-fold cross-validation, you can just follow the instructions in (https://github.com/MIC-DKFZ/nnUNet/blob/master/documentation/how_to_use_nnunet.md).

# Data inference
In data inference phase, we predict the segmentation through:
```python inference.py -i INPUT_FOLDER -o OUTPUT_FOLDER -d DATASET_NAME_OR_ID -c CONFIGURATION```
In which INPUT_FOLDER is the folder where you put data you want to predict, and OUTPUT_FOLDER is the folder where you want to get the corresponding output segmentation.

# Trained model
Our trained model was uploaded to google drive: https://drive.google.com/drive/folders/1XTUI562iNHF2Rhf7H-pzvZEzbGOqsb_w?usp=drive_link. If you want to use it, just download it from the provided link.