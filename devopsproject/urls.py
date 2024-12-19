from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/devopsapp/tickets/', permanent=True)),
    path('devopsapp/', include("devopsapp.urls")),
    path('admin/', admin.site.urls),
    path('devopsapp/login/', RedirectView.as_view(url='/accounts/login/', permanent=True)),
    path('accounts/', include('django.contrib.auth.urls')),
]