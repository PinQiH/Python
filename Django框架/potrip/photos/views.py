from django.shortcuts import render, redirect
from .forms import UploadModelForm
from .models import Photo

def index(request):
    photos = Photo.objects.all()  # 查詢所有資料
    form = UploadModelForm()
    if request.method == "POST":
        form = UploadModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/photos')

    context = {
        'photos': photos,
        'form': form
    }
    return render(request, 'photos/index.html', context)