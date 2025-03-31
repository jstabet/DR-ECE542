# DR-ECE542
Diabetic retinopathy detection for ECE542 course project

## Conda Environment (WIP)
```conda create -n dr pytorch torchvision torchinfo pillow pandas numpy matplotlib seaborn scikit-learn imbalanced-learn tqdm ipykernel```

## Files
```data:```:
* train: raw images from kaggle
* img_stats.npz: npz of image dimensions and max pixel values
* preproc_train_imgs.pth: torch tensor of images preprocessed per resnet
* trainLabels.csv: raw labels from kaggle

```results:```:
> each subfolder contains the following: model.pth, metadata.pth (train/val/test data, training metrics, optimizer), test_results.npz (y_true and y_pred on test set), training_curves.png, and confusion_matrix.png
* baseline: simple CNN
* resnet_random: resnet50, random train/val/test split
* resnet: resnet50, train/val/test stratified by class label

```src:```
* EDA.ipynb: EDA
* preproc.ipynb: preprocess images per resnet and save to memory
* baseline/resnet_random/resnet.ipynb: train models and save model/metadata to memory
* evaluate.ipynb: evaluate model test set
* utils.py: helpful functions (DRDataset class)

## Dataset
[Download from Kaggle](https://www.kaggle.com/competitions/diabetic-retinopathy-detection/data)
>Note: to access training images, unzip into train.zip.00X then run
>```
>cat train.zip.001 train.zip.002 train.zip.003 train.zip.004 train.zip.005 > train.zip
>unzip train.zip
>```

### Labels  
0 - No DR  
1 - Mild  
2 - Moderate  
3 - Severe  
4 - Proliferative DR  