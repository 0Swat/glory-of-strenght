from django.shortcuts import render, redirect
from .forms import LiftVideoForm
from .models import LiftVideo

def Home(request):
    videos = LiftVideo.objects.all().order_by("-date")
    return render(request, 'liftlog/home.html', {'videos': videos})

def upload_video(request):
    if request.method == "POST":
        form = LiftVideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LiftVideoForm()
    return render(request, 'liftlog\upload.html', {'form': form})
