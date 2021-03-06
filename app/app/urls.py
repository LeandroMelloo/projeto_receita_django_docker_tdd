from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/user/', include('user.urls')),
    path('api/v1/recipe/', include('recipe.urls')),
    path('api/v1/', include('reports.urls')),
    path('api/v1/', include('job.urls')),
]
