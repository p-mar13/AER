from celery import shared_task
from .ml_model.image_mode import dan_image
from .ml_model.video_mode import dan_video
import aer.ml_model.video_mode.video_to_frames_divider as vfd
from aer.models import TextFile
import random
import shutil
import os
from django.core.files import File
from datetime import datetime
import os

# Task to detect and classify facial emotions in image
@shared_task(bind=True)
def analyzeFacialEmotionImage(self,data, title):
    current_task_file=open('aer\cache\current_task_file_img.txt','w+')
    current_task_file.write(self.AsyncResult(self.request.id).id) # Update name of the current task
    current_task_file.close()
    path_to_file='media\get_file\\'+str(dan_image.main(data, title))+'.txt' # Initialize FER
    self.update_state(state="COMPLETED", meta={
                 "task_id": self.AsyncResult(self.request.id).id,"file":str(path_to_file), "time":str(datetime.now())
             })
    return self.AsyncResult(self.request.id).result # Return results of executed task

# Task to detect and classify facial emotions in video
@shared_task(bind=True)
def analyzeFacialEmotionVideo(self,vid_title, v_title):
    if(vid_title is None): # Case of video upload issues
        self.update_state(state="ERROR", meta={
                 "description":'file upload error'
             }) 
        return 'upload error'
    self.update_state(state="PROGRESS", meta={ # Task in progress
                 "task_id": self.AsyncResult(self.request.id).id,"current": 0, "total": 0, "percent":0
             }) 
    current_task_file=open('aer\cache\current_task_file_vid.txt','w+')
    current_task_file.write(self.AsyncResult(self.request.id).id) #Update name of the current task
    current_task_file.close()
    unique_file=False
    self.update_state(state="PROGRESS", meta={ # Update progress
                 "task_id": self.AsyncResult(self.request.id).id,"current": 0, "total": 0, "percent":5
             })    
    os.mkdir("aer\ml_model\\video_mode\\frames\\"+str(self.AsyncResult(self.request.id).id))
    fps,frames=vfd.video_divider(str(vid_title),str(self.AsyncResult(self.request.id).id)) # Divide into frames

    self.update_state(state="PROGRESS", meta={ # Update progress
                 "task_id": self.AsyncResult(self.request.id).id,"current": 0, "total": int(frames), "percent":10
             }) 
    filename=str(vid_title)[:-4]
    path_to_file='media\get_file\\'+filename+'.txt'
    new_filename=filename
    while unique_file==False: # Loop to generate unique text file name
        path_to_file='media\get_file\\'+new_filename+'.txt'
        if not os.path.exists(path_to_file):
          fp=open(str(path_to_file),'w+')
          unique_file=True
        else:
          new_filename=filename+str(int(random.random()*10000000))
    self.update_state(state="PROGRESS", meta={ # Update progress
                 "task_id": self.AsyncResult(self.request.id).id,"current": 0, "total": int(frames), "percent":20
             }) 
    all_frames = (int(frames)/16) # Get number of all picked frames
    for x in range(int(all_frames)): # Loop to analyze all frames and get results 
        if x==0:
           img=str("aer\ml_model\\video_mode\\frames\\"+str(self.AsyncResult(self.request.id).id)+"\\frame"+str((x+1))+".jpg")
           dan_video.image_analyzer(img, (x+1), fp, fps)
           img=str("aer\ml_model\\video_mode\\frames\\"+str(self.AsyncResult(self.request.id).id)+"\\frame"+str((x+1)*16)+".jpg")
           dan_video.image_analyzer(img, (x+1)*16, fp, fps)
        else:
           img=str("aer\ml_model\\video_mode\\frames\\"+str(self.AsyncResult(self.request.id).id)+"\\frame"+str((x+1)*16)+".jpg")
           dan_video.image_analyzer(img, (x+1)*16, fp, fps)
        percent_calc=((int(x+1)/int(all_frames))*80)+20
        self.update_state(state="PROGRESS", meta={ 
                 "task_id": self.AsyncResult(self.request.id).id,"current": x+1, "total": int(all_frames), "percent":int(percent_calc)
             })
    temp_file=TextFile() # Create TextFile class for results
    temp_file.data_type='Video'
    temp_file.title=v_title
    temp_file.file=File(open(path_to_file))
    fp.close()
    temp_file.content = str(open(path_to_file).read())
    temp_file.save()
    fp.close()
    self.update_state(state="COMPLETED", meta={ # Progress completed successfuly
                 "current": int(frames), "total": int(frames), "percent":int(100), "file":str(path_to_file), "time":str(datetime.now())
             })
    if os.path.isfile("aer\ml_model\\video_mode\\frames\\"+self.AsyncResult(self.request.id).id+"\\frame16.jpg"):
        shutil.rmtree("aer\ml_model\\video_mode\\frames\\"+self.AsyncResult(self.request.id).id, ignore_errors=True) # Remove directory of task with frames
    return self.AsyncResult(self.request.id).result

