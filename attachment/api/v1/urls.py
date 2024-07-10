from django.urls import path
from .views import *
app_name = 'attachment'

urlpatterns = [
    path('upload_file', UploadFilesApiView.as_view(), name='upload_file'),
]