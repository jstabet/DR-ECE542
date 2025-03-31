import torch
from PIL import Image
import os

class DRDataset(torch.utils.data.Dataset):
    '''
    Dataset class for DR images.
    '''

    def __init__(self, label_df, images_source, preproc=None):

        # set internal variables
        self.label_df = label_df
        self.preproc = preproc
        
        # load images into memory if images_source is a file
        if os.path.isfile(images_source):
            self.images_source = torch.load(images_source)
            self.mem = True
        # set images_source as directory if it is a directory
        else:
            assert os.path.isdir(images_source)
            self.images_source = images_source
            self.mem = False
    
    def __getitem__(self, idx):

        # get subset based on idx
        subset = self.label_df.iloc[idx]
        label = subset['level']
        
        # load image if in memory
        if self.mem:
            img_preproc = self.images_source[subset.name] # subset.name is original index of entire df

        # OR preprocess image
        else:
            img_path = subset['image'] + '.jpeg'
            img = Image.open(os.path.join(self.images_source, img_path))
            img_preproc = self.preproc(img)

        return img_preproc, label
    
    def __len__(self):
        return len(self.label_df)