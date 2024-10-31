from django.contrib import admin
from django.http import HttpRequest
from django.http.response import HttpResponse
from .models import Order
from django.urls import path
from .views import pdforder
from django.shortcuts import redirect
from main.models import Portfolio
from main.models import Sale

# Register your models here.

class Orderadmin(admin.ModelAdmin):
  change_form_template="main/buttonadmin.html"
  def get_urls(self):
    urls=super().get_urls()
    customurls=[path("<int:id>/pdf/",self.admin_site.admin_view(self.pdf),name="pdf"),]
    return customurls+urls
  def change_view(self, request, object_id, form_url='', extra_context=None) -> HttpResponse:
    extra_context=extra_context or {}
    extra_context["custom_button"]=True
    return super().change_view(request, object_id, form_url, extra_context)  
  def pdf(self, request, id):
    obj=self.get_object(request,id)
    print(obj)
    return redirect("pdfconvector", obj.pk)
admin.site.register(Order, Orderadmin)

admin.site.register(Portfolio)
admin.site.register(Sale)
   