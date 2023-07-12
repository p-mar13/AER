import cv2

# Function to divide video into frames
def video_divider(video_name, task_name):   
    vidcap = cv2.VideoCapture("media\\post_videos\\"+video_name) # Open video saved in media location
    frames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    success,image = vidcap.read()
    count = 1
    while success:
        if count%16==0 or count==1: # Save frames no. 1, 16, 32, etc...
            cv2.imwrite("aer\ml_model\\video_mode\\frames\\"+str(task_name)+"\\frame%d.jpg" % count, image)  
        success,image = vidcap.read()
        count += 1
    vidcap.release()
    return fps, frames
