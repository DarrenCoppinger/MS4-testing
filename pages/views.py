from django.shortcuts import render

# Create your views here.


def about(request):
    """Return about.html file"""
    return render(request, 'about.html')
