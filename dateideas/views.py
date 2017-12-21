from django.shortcuts import render, get_object_or_404, redirect
from .models import Ideas
from django.utils import timezone
from .forms import PostForm

# Create your views here.
def date_list(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            ideas = form.save(commit=False)
            ideas.created_date = timezone.now()
            ideas.save()
            ideas = Ideas.objects.all()
            return render(request, 'dateideas/date_list.html', {'ideas': ideas})
        else:
            form = PostForm()
            ideas = Ideas.objects.all()
            return render(request, 'dateideas/date_list.html', {'ideas': ideas})
    else:
        ideas = Ideas.objects.all()
        return render(request, 'dateideas/date_list.html', {'ideas': ideas})

def post_remove(request, pk):
    ideas = get_object_or_404(Ideas, pk=pk)
    ideas.delete()
    return redirect('date_list')
