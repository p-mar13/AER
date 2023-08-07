from PIL import Image
import numpy as np
import cv2
import datetime
import torch
from torchvision import transforms, models

class Model():
    def __init__(self):
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu") #If CUDA available run GPU, otherwise CPU
        self.data_transforms = transforms.Compose([
                                    transforms.Resize((224, 224)),
                                    transforms.ToTensor(),
                                    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                    std=[0.229, 0.224, 0.225])
                                ])
        self.labels = ['neutral', 'happy', 'sad', 'surprise', 'fear', 'disgust', 'anger', 'contempt'] # All emotions that can be recognized
        self.model=  models.resnet18(pretrained=True)
        checkpoint = torch.load(r'aer\ml_model\image_mode\checkpoints\affecnet8_epoch5_acc0.6209.pth',
            map_location=self.device)
        self.model.load_state_dict(checkpoint['model_state_dict'],strict=True)
        self.model.to(self.device)
        self.model.eval()
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    # Detect all faces using OpenCV
    def detect(self, img):
        detected_image = cv2.cvtColor(np.asarray(img),cv2.COLOR_RGB2BGR)
        faces = self.face_cascade.detectMultiScale(detected_image)
        return faces
    # Analyze frame
    def fer(self, path):
        labels=[]
        coordinates=[]
        img0 = Image.open(path).convert('RGB') # Open image
        faces = self.detect(img0)
        if len(faces) == 0:
            return 'null'
        for face_index in range(len(faces)):
            x, y, w, h = faces[face_index]
            img = img0.crop((x,y, x+w, y+h)) # Crop image using coordinates
            img = self.data_transforms(img)
            img = img.view(1,3,224,224)
            img = img.to(self.device)
            with torch.set_grad_enabled(False):
                out, _, _ = self.model(img)
                _, pred = torch.max(out,1)
                index = int(pred)
                label = self.labels[index] # Assign indetified emotion
                labels.append(label) 
                coord=str(x)+', '+str(y)+', '+str(x+w)+', '+str(y+h) # Get coordinates
                coordinates.append(coord)
        return labels, coordinates

# Analyzes single frame
def image_analyzer(image, count, file, fps):
    model = Model() # Create FER model
    label, coordinates = model.fer(image) # Obtain arrays with coordinates and recognized emotions
    seconds = round(count / fps)
    video_time = datetime.timedelta(seconds=seconds)
    for x in range(len(label)): # Create line with information about recognized details
        file.writelines(label[x] +' : ')
        file.writelines(coordinates[x]+' : ')
        file.writelines(str(video_time)+' : ')
        file.writelines("frame"+' '+str(count))
        file.write('\n')




