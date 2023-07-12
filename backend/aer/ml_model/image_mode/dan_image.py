from PIL import Image
import numpy as np
import cv2
from aer.models import TextFile
import torch
from torchvision import transforms
from aer.ml_model.image_mode.network.dan import DAN
import os
from django.core.files import File
import random

class Model():
    def __init__(self):
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.data_transforms = transforms.Compose([
                                    transforms.Resize((224, 224)),
                                    transforms.ToTensor(),
                                    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                    std=[0.229, 0.224, 0.225])
                                ])
        self.labels = ['neutral', 'happy', 'sad', 'surprise', 'fear', 'disgust', 'anger', 'contempt']
        self.model = DAN(num_head=4, num_class=8, pretrained=False)
        checkpoint = torch.load(r'aer\ml_model\image_mode\checkpoints\affecnet8_epoch5_acc0.6209.pth',map_location=self.device)
        self.model.load_state_dict(checkpoint['model_state_dict'],strict=True)
        self.model.to(self.device)
        self.model.eval()
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    
    def detect(self, img0):
        img = cv2.cvtColor(np.asarray(img0),cv2.COLOR_RGB2BGR)
        faces = self.face_cascade.detectMultiScale(img)
        return faces

    def fer(self, path):
        labels=[]
        cooridnates=[]
        path1='media\post_images\\'+path
        img0 = Image.open(path1).convert('RGB')
        faces = self.detect(img0)
        if len(faces) == 0:
            return 'null'
        #  Multiple face detection
        for face_index in range(len(faces)):
            x, y, w, h = faces[face_index]
            img = img0.crop((x,y, x+w, y+h))
            img = self.data_transforms(img)
            img = img.view(1,3,224,224)
            img = img.to(self.device)
            with torch.set_grad_enabled(False):
                out, _, _ = self.model(img)
                _, pred = torch.max(out,1)
                index = int(pred)
                label = self.labels[index]
                labels.append(label)
                coord=str(x)+', '+str(y)+', '+str(w)+ ', '+str(h)
                cooridnates.append(coord)
        return labels, cooridnates

def main(image, image_title):
    unique_file=False
    model = Model()
    labels, coordinates = model.fer(image)
    filename=str(image)[:-4]
    path_to_file='media\get_file\\'+filename+'.txt'
    new_filename=filename
    while unique_file==False:
        path_to_file='media\get_file\\'+new_filename+'.txt'
        if not os.path.exists(path_to_file):
          fp=open(str(path_to_file),'w+')
          unique_file=True
        else:
          new_filename=filename+str(int(random.random()*10000000))
    for x in range(len(labels)):
        fp.writelines(labels[x] +' : ')
        fp.writelines(coordinates[x]+' ')
    temp_file=TextFile()
    temp_file.data_type='Image'
    temp_file.title=image_title
    temp_file.file=File(open(path_to_file))
    fp.close()
    temp_file.content = str(open(path_to_file).read())
    print(temp_file.content)
    temp_file.save()
    fp.close()
    return new_filename
    