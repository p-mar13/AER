from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from aer.models import Image, Video, Email, TextFile

# Unit tests for model Image
class ImageModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Image.objects.create(title='photo')
        Image.image = SimpleUploadedFile(name='test_image.jpg', content=open('testdata\\testimage\\2.jpg', 'rb').read(), content_type='image/jpg')
    
    def testTitleLabel(self):
        image = Image.objects.get(id=1)
        title_field = image._meta.get_field('title').verbose_name
        self.assertEqual(title_field, 'title')

    def testImageLabel(self):
        image = Image.objects.get(id=1)
        image_field = image._meta.get_field('image').verbose_name
        self.assertEqual(image_field, 'image')

    def testTitleMaxLength(self):
        image = Image.objects.get(id=1)
        max_length = image._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)

    def testGetImageSelf(self):
        image = Image.objects.get(id=1)
        self.assertEqual(str(image), 'photo')

# Unit tests for model Video
class VideoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Video.objects.create(title='video')
        Video.image = SimpleUploadedFile(name='test_video.mp4', content=open('testdata\\testvideo\\video.mp4', 'rb').read(), content_type='video/mp4')
    
    def testTitleLabel(self):
        video = Video.objects.get(id=1)
        title_field = video._meta.get_field('title').verbose_name
        self.assertEqual(title_field, 'title')

    def testVideoLabel(self):
        video = Video.objects.get(id=1)
        video_field = video._meta.get_field('image').verbose_name
        self.assertEqual(video_field, 'image')

    def testTitleMaxLength(self):
        video = Video.objects.get(id=1)
        max_length = video._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)

    def testGetVideoSelf(self):
        video = Video.objects.get(id=1)
        self.assertEqual(str(video), 'video')

# Unit tests for model Email
class EmailModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Email.objects.create(name='Test_name', email='Test_email@gmail.com', message='Test_message')

    def testNameLabel(self):
        email = Email.objects.get(id=1)
        name_field = email._meta.get_field('name').verbose_name
        self.assertEqual(name_field, 'name')

    def testEmailLabel(self):
        email = Email.objects.get(id=1)
        email_field = email._meta.get_field('email').verbose_name
        self.assertEqual(email_field, 'email')

    def testMessageLabel(self):
        email = Email.objects.get(id=1)
        title_field = email._meta.get_field('message').verbose_name
        self.assertEqual(title_field, 'message')

    def testNameMaxLength(self):
        email = Email.objects.get(id=1)
        max_length = email._meta.get_field('name').max_length
        self.assertEqual(max_length, 50)

    def testMessageMaxLength(self):
        email = Email.objects.get(id=1)
        max_length = email._meta.get_field('message').max_length
        self.assertEqual(max_length, 1000)

    def testEmailMaxLength(self):
        email = Email.objects.get(id=1)
        max_length = email._meta.get_field('email').max_length
        self.assertEqual(max_length, 50)

    def testGetEmailSelf(self):
        email = Email.objects.get(id=1)
        self.assertEqual(str(email), 'Test_email@gmail.com')

# Unit tests for model TextFile
class TextFileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        TextFile.objects.create(title='Test_title',content='',data_type='')
        TextFile.file = SimpleUploadedFile(name='test_image.jpg', content=open('testdata\\testimage\\2.jpg', 'rb').read(), content_type='image/jpg')
    
    def testTitleLabel(self):
        file = TextFile.objects.get(id=1)
        title_field = file._meta.get_field('title').verbose_name
        self.assertEqual(title_field, 'title')

    def testContentLabel(self):
        file = TextFile.objects.get(id=1)
        content_field = file._meta.get_field('content').verbose_name
        self.assertEqual(content_field, 'content')

    def testCreatedLabel(self):
        file = TextFile.objects.get(id=1)
        created_field = file._meta.get_field('created').verbose_name
        self.assertEqual(created_field, 'created')

    def testDataTypeLabel(self):
        file = TextFile.objects.get(id=1)
        type_field = file._meta.get_field('data_type').verbose_name
        self.assertEqual(type_field, 'data type')

    def testTitleMaxLength(self):
        file = TextFile.objects.get(id=1)
        max_length = file._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)

    def testContentMaxLength(self):
        file = TextFile.objects.get(id=1)
        max_length = file._meta.get_field('content').max_length
        self.assertEqual(max_length, 1000000000)

    def testTextFileSelf(self):
        file = TextFile.objects.get(id=1)
        self.assertEqual(str(file), 'Test_title')
