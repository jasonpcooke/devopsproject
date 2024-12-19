from django.shortcuts import render, redirect
from .models import Ticket
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

class IndexView(LoginRequiredMixin, View):
    @method_decorator(never_cache)
    def get(self, request):
        tickets = Ticket.objects.order_by('-created_at')[:5]
        return render(request, 'index.html', {'tickets': tickets})

class TicketByIdView(LoginRequiredMixin, View):
    @method_decorator(never_cache)
    def get(self, request, ticket_id):
        ticket = Ticket.objects.get(pk=ticket_id)
        return render(request, 'ticket_by_id.html', {'ticket': ticket})

def login_redirect(request):
    messages.error(request, 'You must be logged in to view tickets.')
    return redirect('login')
