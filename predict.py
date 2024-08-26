import torchvision
from torchvision import transforms
from torch.utils.data import (Dataset, DataLoader)
import torch
import os
from torchvision.models import vit_b_32
from torch import nn
from PIL import Image



path = os.environ['MODEL_PATH']
device = torch.device('cpu')
#model = torch.load(path, map_location=device)
model = vit_b_32(weights='DEFAULT')
model.heads = nn.Linear(in_features=768, out_features=25)
state_dict = torch.load(path, map_location=device)
model.load_state_dict(state_dict)
model.to(device)

def transform_image(test_image_path: str)-> torch.utils.data.DataLoader:
    imgtransform = torchvision.transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5,0.5,0.5], std=[0.5,0.5,0.5]),
])
    image = Image.open(test_image_path)
    image = imgtransform(image).unsqueeze(0)
    #test = torchvision.datasets.ImageFolder(root = test_image_path, transform = imgtransform)
    test_loader = DataLoader(image, batch_size=1, shuffle=False)
    return test_loader


classes = ['Asian Green Bee Eater', ' Brown Headed Barbet', ' Cattle Egret', 
           ' Common Kingfisher', 'Common Myna', 'Common Rosefinch', 'Common Tailorbird', 
           'Coppersmith Barbet', 'Forest Wagtail', ' Gray Wagtail','Hoopoe', ' House Crow', 
           ' Indian Grey Hornbill', ' Indian Peacock', ' Indian Pitta', ' Indian Roller','Jungle Babbler', 
           ' Northern Lapwing', 'Red-Wattled Lapwing', 'Ruddy Shelduck', 'Rufous Treepie','Sarus Crane', 
           'White Wagtail', 'White-Breasted Kingfisher', 'White-Breasted Waterhen']  





def predict(testloader: torch.utils.data.DataLoader)-> list: 
    prob = torch.nn.Softmax()
    with torch.no_grad():
        for images in testloader:
            #images = images.to(device)
            #labels = labels.to(device)
            outputs = model(images)
            probability = torch.nn.LogSoftmax(dim=1)(outputs)
            predicted = torch.argmax(outputs.data, 1)
            #total += labels.size(0)
            #correct += (predicted == labels).sum().item()

            predictedclassval, predictedclassindex = torch.max(prob(outputs), 1)
            prob = predictedclassval.item()*100
            predictedclass = classes[predictedclassindex.item()]
    
    return [prob,predictedclass]

test = 'test.jpg'

probability, predict = predict(transform_image(test))
print(probability, predict)