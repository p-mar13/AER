from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from aer.models import Image, Video, Email, TextFile
import aer.views as views
from django.http import HttpRequest

class ImageViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        no_of_images = 5
        for image_id in range(no_of_images):
            Image.objects.create(
                title=f'Photo '+str(image_id),
                image = SimpleUploadedFile(name='test_image{image_id}.jpg', content=open('testdata\\testimage\\2.jpg', 'rb').read(), content_type='image/jpg')
            )

    def testGETURLSAtGivenLocationBeforePOST(self):
        response = self.client.get('/api/images/')
        self.assertEqual(response.status_code, 200)

    def testURLCanBeAcessedByName(self):
        response = self.client.get(reverse('images_list'))
        self.assertEqual(response.status_code, 200)

    def testPOSTURLSRequest(self):
        image = SimpleUploadedFile(name='test_image6.jpg', content=open('testdata\\testimage\\2.jpg', 'rb').read(), content_type='image/jpg')
        response = self.client.post(reverse('images_list'),{ "title":'Photo 6',
                "image" : image,
            })
        self.assertEqual(response.status_code, 200)

    def testPOSTURLSRequestNegative(self):
        image = SimpleUploadedFile(name='test_image6.jpg', content=open('testdata\\testimage\\2.jpg', 'rb').read(), content_type='image/jpg')
        response = self.client.post(reverse('images_list'),{ "image":'Photo 6',
                "title" : image,
            })
        self.assertEqual(response.status_code, 400)

    def testGETURLSAtGivenLocationAfterPOST(self):
        response = self.client.get('/api/images/')
        self.assertEqual(response.status_code, 200)

class VideoViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # 5 videos created for test data
        no_of_videos = 5
        for video_id in range(no_of_videos):
            Video.objects.create(
                title=f'Photo {video_id}',
                image = SimpleUploadedFile(name='test_video{video_id}.mp4', content=open('testdata\\testvideo\\video.mp4', 'rb').read(), content_type='video/mp4')
            )

    def testGETURLSAtGivenLocationBeforePOST(self):
        response = self.client.get('/api/videos/')
        self.assertEqual(response.status_code, 200)

    def testURLCanBeAcessedByName(self):
        response = self.client.get(reverse('videos_list'))
        self.assertEqual(response.status_code, 200)

    def testPOSTURLSRequest(self):
        video = SimpleUploadedFile(name='test_video6.mp4', content=open('testdata\\testvideo\\video.mp4', 'rb').read(), content_type='video/mp4')
        response = self.client.post(reverse('videos_list'),{ "title":'Photo 6',
                "image" : video,
            })
        self.assertEqual(response.status_code, 200)

    def testPOSTURLSRequestNegative(self):
        video = SimpleUploadedFile(name='test_video6.mp4', content=open('testdata\\testvideo\\video.mp4', 'rb').read(), content_type='video/mp4')
        response = self.client.post(reverse('images_list'),{ "image":'Photo 6',
                "title" : video,
            })
        self.assertEqual(response.status_code, 400)

    def testGETURLSAtGivenLocationAfterPOST(self):
        response = self.client.get('/api/videos/')
        self.assertEqual(response.status_code, 200)

class EmailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # 5 email messages created for test data
        no_of_emails = 5
        for email_id in range(no_of_emails):
            Email.objects.create(
                name=f'Name {email_id}',
                email=f'Email {email_id}',
                message=f'Message {email_id}',
            )

    def testGETURLSAtGivenLocationBeforePOST(self):
        response = self.client.get('/api/email/')
        self.assertEqual(response.status_code, 200)

    def testURLCanBeAcessedByName(self):
        response = self.client.get(reverse('email'))
        self.assertEqual(response.status_code, 200)

    def testPOSTURLSRequest(self):
        response = self.client.post(reverse('email'),{ "name":'Test',
                "email" : "Email@mgail.com", "message" : "Message test 1.",
            })
        self.assertEqual(response.status_code, 200)

    def testPOSTURLSRequestNegative1(self):
        image = SimpleUploadedFile(name='test_video6.mp4', content=open('testdata\\testvideo\\video.mp4', 'rb').read(), content_type='video/mp4')
        response = self.client.post(reverse('email'),{ "name":'Neg_Test2',
                "email" : "Neg@gmail.com", "message" : image,
            })
        self.assertEqual(response.status_code, 400)

    def testPOSTURLSRequestNegative2(self):
        char_array=[]
        for x in range(102):
            char_array.append('a')
        response = self.client.post(reverse('email'),{ "name":'Neg_Test2',
                "email" : str(char_array), "message" : "Message 123. Test 1233.",
            })
        self.assertEqual(response.status_code, 400)

    def testGETURLSAtGivenLocationAfterPOST(self):
        response = self.client.get('/api/email/')
        self.assertEqual(response.status_code, 200)

class TextFileViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # 3 TextFile objects created for test data
        f = SimpleUploadedFile(name='file.txt', content=open('testdata\\testfile\\face.txt', 'rb').read(), content_type='file/txt')
        for file_id in range(2):
            TextFile.objects.create(
                title=f'Title {file_id}',
                content='happy : 839, 99, 667, 667',
                file=f,
                data_type='Image')
        TextFile.objects.create(
                title='Title 3',
                content='happy : 839, 99, 667, 667',
                file=f,
                data_type='Video'
            )

    def testGETURLSAtGivenLocationBeforePOST(self):
        response = self.client.get('/api/textfile/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/api/textfile/image')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/api/textfile/video')
        self.assertEqual(response.status_code, 200)
        response = self.client.delete('/api/textfile/2')
        self.assertEqual(response.status_code, 200)

    def testURLSCanBeAcessedByName(self):
        response = self.client.get(reverse('image_files'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('video_files'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('textfile_list'))
        self.assertEqual(response.status_code, 200)

    def testDeleteRequest(self):
        file = TextFile.objects.get(pk=1)
        self.assertEqual(str(file),'Title 0')
        request=HttpRequest()
        request.method='DELETE'
        response=views.deleteEntry(request,1)
        self.assertEqual(response.status_code, 200)

class TaskViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        no_of_t = 3

    def testFunctionGetTaskDataNegative(self):
        response=views.getTaskData('ced9e48d-3ba9-400b-8823-3e9ba6cc4c30')
        self.assertEqual(response['state'], 'ERROR')
        response=views.getTaskData('xxx')
        self.assertEqual(response['state'], 'ERROR')

    def testGETProgressURLSAtGivenLocationNegative(self):
        response = self.client.get('/api/task_progress/')
        self.assertEqual(response.status_code, 404)

    def testGETTaskURLSAtGivenLocationNegative(self):
        response = self.client.get('/api/task_details/2')
        self.assertEqual(response.status_code, 404)


