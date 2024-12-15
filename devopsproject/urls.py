from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('devopsapp/', include("devopsapp.urls")),
    path('admin/', admin.site.urls),
]