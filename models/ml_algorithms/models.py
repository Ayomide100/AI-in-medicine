import io
import numpy as np
from torch.autograd import Variable
import torch
import torch.nn as nn
from torchvision import models
from PIL import Image
import torchvision.transforms as transforms
from collections import OrderedDict
from views import app, back


# Load a checkpoint and rebuild the model
def load_checkpoint(filepath):
    checkpoint = torch.load(filepath)
    model = checkpoint['model']
    model.sched = checkpoint['scheduler']
    model.classifier = checkpoint['classifier']
    model.load_state_dict(checkpoint['state_dict'])
    model.class_to_idx = checkpoint['class_to_idx']
    optimizer = checkpoint['optimizer']
    epochs = checkpoint['epochs']
    
    for param in model.parameters():
        param.requires_grad = False
        
    return model, checkpoint['class_to_idx']


def get_tensor(image):
    
    #Applying transforms on the Image
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], 
                             std=[0.229, 0.224, 0.225])
    ])
    image = preprocess(image).unsqueeze(0)
    return image



    #return my_transforms(image).unsqueeze(0)


model, class_to_idx = load_checkpoint('C:/Users/Test/Desktop/ai in med/models/checkpoint.pth')
model.eval()


def diagnosis_type(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    classes = ('Athsma', 'covid-19', 'normal', 'viral pneumonia')
    tensor = get_tensor(image)
    outputs = model(tensor)
    _, prediction = torch.max(outputs,1)
    category = prediction.item()
    name = classes[category]
    return  name


    """tensor = get_tensor(image_bytes)
    outputs = model(tensor)
    _, prediction = torch.max(outputs,1)
    category = prediction.item()
    name = classes[category]
    return  name"""
    