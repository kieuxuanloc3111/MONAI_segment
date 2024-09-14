# import pytorch_lightning
# from monai.utils import set_determinism
# from monai.transforms import (
#     AsDiscrete,
#     EnsureChannelFirstd,
#     Compose,
#     CropForegroundd,
#     LoadImaged,
#     Orientationd,
#     RandCropByPosNegLabeld,
#     ScaleIntensityRanged,
#     Spacingd,
#     EnsureType,
# )
# from monai.networks.nets import UNet
# from monai.networks.layers import Norm
# from monai.metrics import DiceMetric
# from monai.losses import DiceLoss
# from monai.inferers import sliding_window_inference
# from monai.data import CacheDataset, list_data_collate, decollate_batch, DataLoader
# from monai.config import print_config
from monai.apps import download_and_extract
# import torch
# import matplotlib.pyplot as plt
# import tempfile
# import shutil
import os
import glob

# print_config()

# directory = os.environ.get("MONAI_DATA_DIRECTORY")
# if directory is not None:
#     os.makedirs(directory, exist_ok=True)
# root_dir = tempfile.mkdtemp() if directory is None else directory
# print(root_dir)
root_dir=  "/home/vkuai/loc"

resource = "https://msd-for-monai.s3-us-west-2.amazonaws.com/Task09_Spleen.tar"
md5 = "410d4a301da4e5b2f6f86ec3ddba524e"

compressed_file = os.path.join(root_dir, "Task09_Spleen.tar")
data_dir = os.path.join(root_dir, "Task09_Spleen")
if not os.path.exists(data_dir):
    download_and_extract(resource, compressed_file, root_dir, md5)