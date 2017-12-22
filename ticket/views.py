from django.shortcuts import render
from .models import Ticket
from .forms import FormTicket

def add_ticket(request):
    if request.method == "POST":
        form = FormTicket(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user_id = request.user.id
            form.save()
    else:
        form = FormTicket()
    return render(request, "ticket/add_ticket.html", {"form": form})
