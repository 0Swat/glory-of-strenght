from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection
from django.contrib import messages
from .models import LiftAttempt
from .forms import LiftAttemptForm

def _table_exists(model):
    # Fallback jeśli serwer uruchomiono przed migracjami
    return model._meta.db_table in connection.introspection.table_names()

def index(request):
    attempts = []
    table_ready = _table_exists(LiftAttempt)
    if table_ready:
        attempts = LiftAttempt.objects.all()
    return render(request, 'lifts/index.html', {'attempts': attempts, 'table_ready': table_ready})

def add_attempt(request):
    if request.method == 'POST':
        form = LiftAttemptForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Dodano nowe podejście.")
            return redirect('index')
    else:
        form = LiftAttemptForm()
    return render(request, 'lifts/add.html', {'form': form})

def attempt_detail(request, pk):
    attempt = get_object_or_404(LiftAttempt, pk=pk)
    return render(request, 'lifts/detail.html', {'attempt': attempt})

def attempt_delete(request, pk):
    attempt = get_object_or_404(LiftAttempt, pk=pk)
    if request.method == 'POST':
        attempt.delete()
        messages.success(request, "Usunięto próbę.")
        return redirect('index')
    # GET -> confirm page
    return render(request, 'lifts/confirm_delete.html', {'attempt': attempt})
