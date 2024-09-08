from django.forms import ModelForm
from login.models import Review

class ReviewForm(ModelForm):
  class Meta:
    model = Review
    fields =  ['originalfoto', 'text']
