from django.shortcuts import render
from .models import BlogIndexPage

# Create your views here.
def tag_view(request, tag):
    index = BlogIndexPage.objects.first()
    return index.serve(request, tag=tag)