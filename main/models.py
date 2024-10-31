from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

class Order(models.Model):
  name=models.CharField(verbose_name="ФИО", max_length=100)
  phone=PhoneNumberField(verbose_name="телефон", region="RU")
  frame=models.CharField(verbose_name="оправа", max_length=50)
  lenses=models.CharField(verbose_name="линзы", max_length=50)
  price_master=models.CharField(verbose_name="работа мастера", max_length=50)
  sale=models.DecimalField(verbose_name="скидка", decimal_places=2, max_digits=3)
  total=models.FloatField(verbose_name="итого")
  date=models.DateField(verbose_name="дата приема заказа", auto_now=False, auto_now_add=True)
  date_productione=models.DateField(verbose_name="дата изготовления заказа", auto_now=False, auto_now_add=False)
  DDP=models.FloatField(verbose_name="DDP")
  OD_SPH=models.FloatField(verbose_name="OD_SPH")
  OD_CYL=models.FloatField(verbose_name="OD_CYL")
  OD_AX=models.FloatField(verbose_name="OD_AX")
  OS_SPH=models.FloatField(verbose_name="OS_SPH")
  OS_CYL=models.FloatField(verbose_name="OS_CYL")
  OS_AX=models.FloatField(verbose_name="OS_AX")
  class Meta:
    verbose_name="Заказ"
    verbose_name_plural="Заказы"
    ordering = ["-date"] # фильтрация заказов по дате, от новых к старым
  def __str__(self) -> str:
    return "Заказ на очки №" + str(self.id)

class Portfolio(models.Model):
  originalfoto=models.ImageField(upload_to='image', verbose_name="фото")
  foto=ImageSpecField(source='originalfoto', format='PNG', processors=[ResizeToFit(800,800)])
  text=models.TextField(verbose_name='описание')

  class Meta:
   verbose_name="наша работа"
   verbose_name_plural="наши работы"
   
  def __str__(self) -> str:
    return "работа " + str(self.id)
  
class Sale(models.Model):
  originalfoto=models.ImageField(upload_to='image', verbose_name="фото")
  foto=ImageSpecField(source='originalfoto', format='PNG', processors=[ResizeToFit(800,800)])
  text=models.TextField(verbose_name=' акции')

  class Meta:
    verbose_name="наша акция"
    verbose_name_plural="наши акции"
   
  def __str__(self) -> str:
    return "акция" + str(self.id)