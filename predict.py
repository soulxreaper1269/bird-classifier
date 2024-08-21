from torchvision import transforms
from torchvision.utils import Dataloader
import torch
import os

path = os.environ['MODEL_PATH']
device = torch.device('cpu')
model = torch.load(path, map_location=device)

def predict(testloader: torch.DataLoader):
    with torch.no_grad():
        for (images, labels) in test_loader:
            images = images.to(device)
            labels = labels.to(device)
            outputs = model(images)
            probability = torch.nn.LogSoftmax(dim=1)(outputs)
            predicted = torch.argmax(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()



            #print(outputs)
            #print("shape:", outputs.shape)
            predictedclassval, predictedclassindex = torch.max(prob(outputs), 1)
            print(f'predicted class probability:{predictedclassval.item()*100}%')
            #print("max val (probability of class):", predictedclassval)
            predictedclass = classes[predictedclassindex.item()]
            #print("Logits:\n", outputs)
            #print("Probabilities:\n", probability)
            print("Predicted Classes:\n", predictedclass)
            actuallabel = classes[labels.item()]
            print("Actual Labels:\n", actuallabel)
            print("----------")


        #print("Actual Labels:\n", labels)
        print("----------")
    print('Accuracy of the network on the test images: %d %%' % (100 * correct / total))


