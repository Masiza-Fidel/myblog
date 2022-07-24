from django.shortcuts import render
from .models import Blogs
# Create your views here.
def index(request):
    posts =Blogs.objects.all()
    return render(request,"index.html",{'posts':posts})