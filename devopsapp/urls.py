from django.urls import path
from . import views

urlpatterns = [
    path('tickets', views.index, name='index'),
    path('tickets/<int:ticket_id>', views.ticket_by_id, name='ticket_by_id')
]
