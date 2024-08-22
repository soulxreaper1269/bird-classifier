from torchvision import transforms
from torch.utils.data import (Dataset, DataLoader)
import torch
import os

path = os.environ['MODEL_PATH']
device = torch.device('cpu')
model = torch.load(path, map_location=device)

classes = ['Asian Green Bee Eater', ' Brown Headed Barbet', ' Cattle Egret', 
           ' Common Kingfisher', 'Common Myna', 'Common Rosefinch', 'Common Tailorbird', 
           'Coppersmith Barbet', 'Forest Wagtail', ' Gray Wagtail','Hoopoe', ' House Crow', 
           ' Indian Grey Hornbill', ' Indian Peacock', ' Indian Pitta', ' Indian Roller','Jungle Babbler', 
           ' Northern Lapwing', 'Red-Wattled Lapwing', 'Ruddy Shelduck', 'Rufous Treepie','Sarus Crane', 
           'White Wagtail', 'White-Breasted Kingfisher', 'White-Breasted Waterhen']  

def predict(testloader: torch.DataLoader):
    prob = torch.nn.Softmax()
    with torch.no_grad():
        for (images, labels) in testloader:
            images = images.to(device)
            labels = labels.to(device)
            outputs = model(images)
            probability = torch.nn.LogSoftmax(dim=1)(outputs)
            predicted = torch.argmax(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

            predictedclassval, predictedclassindex = torch.max(prob(outputs), 1)
            prob = predictedclassval.item()*100
            predictedclass = classes[predictedclassindex.item()]
