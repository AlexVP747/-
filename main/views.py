from django.shortcuts import render, HttpResponseRedirect
from login.models import Review, Portfolio
from main.forms import ReviewForm
from django.http import HttpResponse
from main.models import Order
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont



def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def lensess(request):
    return render(request, 'main/lensess.html')

def sale(request):
    return render(request, 'main/sale.html')

def portfolio(request):
    portfolio=Portfolio.objects.all()
    context={
        "list":portfolio, 
    }
    return render(request, 'main/portfolio.html', context)

def frame(request):
    return render(request, 'main/frame.html')

def organizations(request):
    return render(request, 'main/organizations.html')



def review(request):
    rev=Review.objects.all()
    context={
        "list":rev, 
        "form":ReviewForm()
    }
    return render(request, 'main/review.html', context)

def addreview(request):
    if request.method=='POST':
        form=ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            obj=Review(**form.cleaned_data) # ** - создает именованные аргументы
            obj.answer=1 # заплатка, позже исправить
            obj.user=request.user 
            obj.save()
            return HttpResponseRedirect('/review')
        else:
            return HttpResponse(form.as_p() )
    else:
        return HttpResponse (ReviewForm().as_p()   )
    
def deletreview(request, idobj):
    if request.method=='POST':
        Review.objects.get(id=idobj).delete()
    return HttpResponseRedirect('/review')
        
def pdforder(request, id):
    order=Order.objects.get(id=id)
    titleOrder=str(id)+".pdf"
    response = HttpResponse(content_type="application/pdf")
    response['Content-Disposition'] = f'attachment; filename="{titleOrder}"'

    # Создаем объект Canvas для генерации PDF
    p = canvas.Canvas(response, pagesize=A4)
    width, height = A4
    logo="main/static/main/img/logo.png"

    # Убедись, что у тебя есть файл Times New Roman.ttf в доступной директории
    pdfmetrics.registerFont(TTFont('TimesNewRoman', 'main/static/main/fonts/timesnewromanpsmt.ttf'))
    p.setFont('TimesNewRoman', 12)

    # Записываем информацию о книге в PDF
    p.drawImage(logo,(width-50)/2, height - 50, width=100, height=50)
    p.drawString(100, height - 100, f"ФИО: {order.name}")
    p.drawString(100, height - 120, f"Телефон: {order.phone}")
    p.drawString(100, height - 140, f"Оправа: {order.frame}")
    p.drawString(100, height - 160, f"Линзы: {order.lenses}")
    p.drawString(100, height - 180, f"Работа мастера: {order.price_master}")
    p.drawString(100, height - 200, f"Скидка: {order.sale}")
    p.drawString(100, height - 220, f"Итого: {order.total}")
    p.drawString(100, height - 240, f"дата приёма заказа: {order.date}")
    p.drawString(100, height - 260, f"дата изготовления заказа: {order.date_productione}")
    p.drawString(100, height - 280, f"DDP: {order.lenses}")
    p.drawString(100, height - 300, f"OD_SPH: {order.OD_SPH}")
    p.drawString(100, height - 320, f"OD_CYL: {order.OD_CYL}")
    p.drawString(100, height - 340, f"OD_AX: {order.OD_AX}")
    p.drawString(100, height - 360, f"OS_SPH: {order.OS_SPH}")
    p.drawString(100, height - 380, f"OS_CYL: {order.OS_CYL}")
    p.drawString(100, height - 400, f"OS_AX: {order.OS_AX}")
   

    p.setTitle(titleOrder)

    # Завершаем генерацию PDF
    p.showPage()
    p.save()

    return response        
    
          