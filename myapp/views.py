from django.shortcuts import render, redirect
from .forms import PostForm

def home(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'home.html', {'form': form})


