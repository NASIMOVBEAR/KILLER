from django.shortcuts import render

# Create your views here.
def killer (req):
    return render (req,'index.html')
def compo (req):
    return render (req,'components.html')