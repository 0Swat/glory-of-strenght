from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection
from django.contrib import messages
from .models import LiftAttempt, LiftType
from .forms import LiftAttemptForm

def _table_exists(model):
    # Fallback jeśli serwer uruchomiono przed migracjami
    return model._meta.db_table in connection.introspection.table_names()

def index(request):
    attempts = []
    table_ready = _table_exists(LiftAttempt)
    filters = {}
    sort = request.GET.get('sort', 'weight_desc')  # domyślnie najcięższe na górze

    if table_ready:
        qs = LiftAttempt.objects.all()

        # Filtrowanie tylko po rodzaju boju
        lift_type = request.GET.get('type', '').strip()
        if lift_type in dict(LiftType.choices):
            qs = qs.filter(lift_type=lift_type)
            filters['type'] = lift_type

        # Sortowanie tylko po ciężarze
        sort = request.GET.get('sort')
        if sort not in ('weight_desc', 'weight_asc'):
            sort = 'weight_desc'
            
        sort_map = {
            'weight_desc': '-weight_kg',
            'weight_asc': 'weight_kg',
        }
        qs = qs.order_by(sort_map[sort])

        attempts = qs

    return render(request, 'lifts/index.html', {
        'attempts': attempts,
        'table_ready': table_ready,
        'filters': filters,
        'sort': sort,
        'lift_types': LiftType.choices,
    })

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
