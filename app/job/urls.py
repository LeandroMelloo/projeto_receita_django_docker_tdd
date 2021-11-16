from django.urls import path

from .views import JobAPIView

# endpoints
urlpatterns = [
    path('job/', JobAPIView.as_view(), name='job'),
]
