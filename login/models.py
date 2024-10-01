from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Review(models.Model):
  originalfoto=models.ImageField(upload_to='image', verbose_name="своё фото")
  foto=ImageSpecField(source='originalfoto', format='PNG', processors=[ResizeToFit(200,200)])
  text=models.TextField(verbose_name='текст')
  user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='reviews', verbose_name='пользователь')
  answer=models.IntegerField(verbose_name='ответ')
  date=models.DateField(verbose_name="дата отзыва", auto_now=False, auto_now_add=True)

  class Meta:
    verbose_name="отзыв"
    verbose_name_plural="отзывы"
    ordering = ["-date"] # фильтрация отзыва по дате

  def __str__(self) -> str:
    return "отзыв" + str(self.id)

class Portfolio(models.Model):
  originalfoto=models.ImageField(upload_to='image', verbose_name="фото")
  foto=ImageSpecField(source='originalfoto', format='PNG', processors=[ResizeToFit(200,200)])
  text=models.TextField(verbose_name='описание')

  class Meta:
   verbose_name="наша работа"
   verbose_name_plural="наши работы"
   
  def __str__(self) -> str:
    return "работа " + str(self.id)
  
class Profile(models.Model):
  originalfoto=models.ImageField(upload_to='image', verbose_name="своё фото")
  foto=ImageSpecField(source='originalfoto', format='PNG', processors=[ResizeToFit(200,200)])
  date=models.DateField(verbose_name="дата рождения", auto_now=False, auto_now_add=False, null=True)
  firstname=models.CharField(max_length=20, verbose_name="имя")
  lastname=models.CharField(max_length=20, verbose_name="фамилия")
  user=models.OneToOneField(User, related_name="Profile", on_delete=models.CASCADE, null=True)
@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(user=instance)
@receiver(post_save, sender=User)
def saveProfile(sender, instance, **kwargs):
  instance.Profile.save()