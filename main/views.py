from django.shortcuts import render, HttpResponseRedirect
from login.models import Review
from main.forms import ReviewForm


def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def lensess(request):
    return render(request, 'main/lensess.html')

def news(request):
    return render(request, 'main/news.html')

def portfolio(request):
    return render(request, 'main/portfolio.html')

def review(request):
    rev=Review.objects.all()
    context={
        "list":rev, 
        "form":ReviewForm()
    }
    return render(request, 'main/review.html', context)

def addreview(request):
    if request.method=='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            obj=Review(**form.cleaned_data) # ** - создает именованные аргументы
            obj.answer=1 # заплатка, позже исправить
            obj.user=request.user 
            obj.save()
    return HttpResponseRedirect('/review')       