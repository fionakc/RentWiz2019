from django.shortcuts import get_object_or_404, redirect, render
from .forms import PostForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()
    return render(request, 'create_listing.html', {'form': form})

