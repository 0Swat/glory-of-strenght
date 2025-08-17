from django.shortcuts import render, redirect
from django.db import connection
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
        form = LiftAttemptForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = LiftAttemptForm()
    return render(request, 'lifts/add.html', {'form': form})
