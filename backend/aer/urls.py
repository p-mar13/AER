from django.urls import path
from . import views

# Urls for REST API
urlpatterns = [
    path('images/', views.ImageView.as_view(), name= 'images_list'),
    path('videos/', views.VideoView.as_view(), name= 'videos_list'),
    path('textfile/', views.getAllFiles, name= 'textfile_list'),
    path('download/', views.DownloadPDF, name='download_pdf'),
    path('email/', views.EmailView.as_view(), name='email'),
    path('progress/', views.getProgress, name='task_progress'),
    path('task/<str:t_id>/', views.getTask, name='task_details'),
    path('textfile/image',views.getImageFiles,name='image_files'),
    path('textfile/video',views.getVideoFiles,name='video_files'),
    path('textfile/<int:pk>',views.deleteEntry,name='delete'),
]