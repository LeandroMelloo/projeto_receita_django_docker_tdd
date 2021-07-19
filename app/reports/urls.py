from django.urls import path

from .views import ReportAPIView

# endpoints
urlpatterns = [
    path('reports/', ReportAPIView.as_view(), name='reports'),
]
