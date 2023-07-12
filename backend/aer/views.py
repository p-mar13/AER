from .serializers import ImageSerializer, VideoSerializer, TextFileSerializer, EmailSerializer
from .models import Image, Video, TextFile, Email
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from django.http import HttpResponse
from .task import analyzeFacialEmotionImage, analyzeFacialEmotionVideo
from rest_framework.decorators import api_view
from django.core.files import File
from django.core.mail import send_mail, BadHeaderError
from celery.result import AsyncResult
import json
FILE_TITLE=''

class ImageView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs): # Get all images
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs): # Post image and initiate FER
        images_serializer = ImageSerializer(data=request.data)
        if images_serializer.is_valid():
            images_serializer.save()
            # Get fields for Image model
            image_title=request.data.get("title",'')
            url=request.data.get("image",'')
            global FILE_TITLE
            FILE_TITLE='IMAGE'
            link_url=str(url)
            if str(url).endswith(".jpg") or str(url).endswith(".png"):
                analyzeFacialEmotionImage.delay(link_url, image_title) # Create asynch task
            else:
                response_data={
                    "state":"ERROR",
                    "description":"upload error: incorrect format of image"
                }
                return HttpResponse(json.dumps(response_data), content_type='application/json', status=400)
            response_data={
                    "state":"SUCCESS",
                    "description":"upload: successful"
                }
            return HttpResponse(json.dumps(response_data), content_type='application/json')
        else:
            response_data={
                    "state":"ERROR",
                    "description":"upload error: upload unsuccessful"
                }
            return HttpResponse(json.dumps(response_data), content_type='application/json', status=400)

class VideoView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs): # Post video and initiate FER
        videos_serializer = VideoSerializer(data=request.data)
        if videos_serializer.is_valid():
            videos_serializer.save()
            # Get fields for Video model
            vid_title=request.data.get("title",'')
            url=request.data.get("image",'')
            global FILE_TITLE
            FILE_TITLE='VIDEO'
            link_url=str(url)
            if str(url).endswith(".mp4") or str(url).endswith(".avi") or str(url).endswith(".mkv"):
                analyzeFacialEmotionVideo.delay(link_url, vid_title) # Create asynch task
            else:
                response_data={
                    "state":"ERROR",
                    "description":"upload error: incorrect format of image"
                }
                return HttpResponse(json.dumps(response_data), content_type='application/json', status=400)
            response_data={
                    "state":"SUCCESS",
                    "description":"upload: successful"
                }
            return HttpResponse(json.dumps(response_data), content_type='application/json')
        else:
            print('error', videos_serializer.errors)
            response_data={
                    "state":"ERROR",
                    "description":"upload error: upload unsuccessful"
                }
            return HttpResponse(json.dumps(response_data), content_type='application/json', status=400)

class EmailView(APIView):
    def get(self, request, *args, **kwargs): # Get all messages
        email = Email.objects.all()
        serializer = EmailSerializer(email, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        subject = "Website Inquiry" 
        mail_serializer = EmailSerializer(data=request.data)
        if mail_serializer.is_valid(): # Check if valid serialized data
            mail_serializer.save()
            body={
            'name':str(request.data.get("name",'')),
            'email':str(request.data.get("email",'')),
            'message':str(request.data.get("message",'')),
            }
            message = "\n".join(body.values())
            # Try to send using Django's mail protocol
            try:
                 send_mail(subject, message, 'p.markiewicz1999@gmail.com', ['p.markiewicz1999@gmail.com'])
            except BadHeaderError:
                response_data={
                    "state":"ERROR",
                    "description":"error: mail could not be sent"
                }
                return HttpResponse(json.dumps(response_data), content_type='application/json', status=400)
            response_data={
                    "state":"SUCCESS",
                    "description":"mail sent successfuly"
                }
            return HttpResponse(json.dumps(response_data), content_type='application/json')
        response_data={
                    "state":"ERROR",
                    "description":"c"
                }
        return HttpResponse(json.dumps(response_data), content_type='application/json', status=400)
        
class TextFileView(APIView):
    parser_classes = (MultiPartParser, FormParser) 
    def get(self, request, *args, **kwargs): # Get all text files
        posts = TextFile.objects.all()
        textSerializer = TextFileSerializer(posts, many=True)
        return Response(textSerializer)
    
@api_view(['DELETE'])
def deleteEntry(request, pk): # Delete request for file
    try:
        result_file = TextFile.objects.get(pk=pk) # Verify if file from request exists
    except result_file.DoesNotExist:
        response_data={
                    "state":"ERROR",
                    "description":"entry does not exist"
                }
        return HttpResponse(json.dumps(response_data), content_type='application/json', status=400)
    if  request.method == 'DELETE':
        result_file.delete()
        response_data={
                    "state":"SUCCESS",
                    "description":"entry deleted successfuly"
                }
        return HttpResponse(json.dumps(response_data), content_type='application/json')

@api_view(['GET'])
def getAllFiles(request): # Get all txt files
    if request.method == 'GET':
        data = TextFile.objects.all().order_by('-created')

        serializer = TextFileSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def getImageFiles(request): # Get txt files for images
    if request.method == 'GET':
        data = TextFile.objects.all().filter(data_type='Image').order_by('-created')

        serializer = TextFileSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
    
@api_view(['GET']) # Get txt files for videos
def getVideoFiles(request):
    if request.method == 'GET':
        data = TextFile.objects.all().filter(data_type='Video').order_by('-created')

        serializer = TextFileSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def DownloadPDF(self): #send current txt file as downloadable to client
    if FILE_TITLE=='IMAGE':
        with open('aer\cache\current_task_file_img.txt','r') as current_task_file:
            task_id=AsyncResult(current_task_file.read())
        current_task_file.close()
    else:
        with open('aer\cache\current_task_file_vid.txt','r') as current_task_file:
            task_id=AsyncResult(current_task_file.read())
        current_task_file.close()
    path_to_file=str(task_id.info['file'])
    f = open(path_to_file, 'rb')
    txtFile = File(f)
    response = HttpResponse(txtFile.read())
    response['Content-Disposition'] = 'attachment'
    return response

@api_view(['GET'])
def getProgress(request): # Send progress of current task
    with open('aer\cache\current_task_file_vid.txt','r') as current_task_file:
        task_id_given=AsyncResult(current_task_file.read())
    current_task_file.close()
    response_data=getTaskData(task_id_given)
    return HttpResponse(json.dumps(response_data), content_type='application/json')

@api_view(['GET']) # Get task of given task name
def getTask(request, t_id):
    response_data=getTaskData(t_id)
    return HttpResponse(json.dumps(response_data), content_type='application/json')

def getTaskData(t_id): # Get data of given task
    try:
        curr_task = AsyncResult(t_id) 
        percent=curr_task.info['percent']
    except TypeError: # Task does not exist
        response_data={'state': 'ERROR',
            'description':'error: task does not exist'}
        return response_data
    if(int(curr_task.info['percent'])==100):
        response_data = {
            'task_id': str(curr_task),
            'percent': curr_task.info['percent'],
            'state' : curr_task.state,
            "file":str(curr_task.info['file']),
        }
    else:
        response_data = {
            'task_id': str(curr_task),
            'percent': curr_task.info['percent'],
            'state' : curr_task.state,
        }   
    return response_data