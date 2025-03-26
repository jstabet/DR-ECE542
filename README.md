# DR-ECE542
Diabetic retinopathy detection for ECE542 course project

## Conda Environment (WIP)
```conda create -n dr torch torchvision torchinfo pillow pandas numpy matplotlib scikit-learn```

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