from django.shortcuts import render, get_object_or_404, redirect
from .models import Ideas
from django.utils import timezone
from .forms import PostForm
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import IdeaSerializer

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

@api_view(['GET', 'POST'])
def idea_list(request, format=None):
    """
    List all code ideas, or create a new idea.
    """
    if request.method == 'GET':
        ideas = Ideas.objects.all()
        serializer = IdeaSerializer(ideas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = IdeaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def idea_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code idea.
    """
    try:
        idea = Ideas.objects.get(pk=pk)
    except Ideas.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = IdeaSerializer(idea)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = IdeaSerializer(idea, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        idea.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
