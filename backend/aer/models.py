from django.db import models

#model for Video class, contains uploaded video file and title given by the user
class Video(models.Model):
    title = models.CharField(max_length=100)
    image = models.FileField(upload_to='post_videos')
    def __str__(self):
        return self.title

#model for Image class, contains uploaded image file and title given by the user
class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.FileField(upload_to='post_images')
    def __str__(self):
        return self.title

 #model for Text File class, contains uploaded text file and its details   
class TextFile(models.Model):
    title = models.CharField(max_length=100)
    content=models.CharField(max_length=1000000000)
    file = models.FileField(upload_to='get_file')
    created = models.DateTimeField(auto_now_add=True) #automatically added date of creation
    data_type=models.CharField(max_length=5) #Image or Video
    ordering_fields = '__all__'
    def __str__(self):
        return self.title

 #model for Email class, contains information about message sent by the user  
class Email(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    message=models.CharField(max_length=1000)
    def __str__(self):
        return self.email