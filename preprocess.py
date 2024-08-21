import torch
import torchvision
from torchvision import transforms
from torch.utils.data import DataLoader

def transform_image(test_image):
    imgtransform = torchvision.transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5,0.5,0.5], std=[0.5,0.5,0.5]),
])

    test_loader = DataLoader(test_image, transform = imgtransform)