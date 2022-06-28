from django.shortcuts import render, redirect
from .forms import CustomerModelForm

def index(request):
    form = CustomerModelForm()
    if request.method == "POST":
        form = CustomerModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/customers')

    context = {
        'form': form
    }
    return render(request, 'customers/index.html', context)