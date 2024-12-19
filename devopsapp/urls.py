from django.urls import path
from django.contrib.auth import views as auth_views
from .views import IndexView, TicketByIdView, login_redirect
from django.views.generic import RedirectView

urlpatterns = [
    path('tickets/', IndexView.as_view(), name='index'),
    path('tickets/<int:ticket_id>/', TicketByIdView.as_view(), name='ticket_by_id'),
    path('login/', RedirectView.as_view(url='/accounts/login/', permanent=True)),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login_redirect/', login_redirect, name='login_redirect'),
]
