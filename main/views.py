from django.shortcuts import render
from login.models import Review


def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def review(request):
    rev=Review.objects.all()
    context={
        "list":rev
    }
    return render(request, 'main/review.html', context)
