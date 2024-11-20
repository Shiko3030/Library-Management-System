from django.contrib.auth.forms import UserCreationForm
from django.forms  import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import *


 

class CategoryForm(ModelForm):
    class Meta :
        model = Category
        fields= ['name']
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control'})
        }



class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets ={
            'category':forms.Select(attrs={'class':'form-control'}),
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'authoer':forms.TextInput(attrs={'class':'form-control'}),
            'photo_book':forms.FileInput(attrs={'class':'form-control'}),
            'photo_authoer':forms.FileInput(attrs={'class':'form-control'}),
            'pages':forms.NumberInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'retal_price_day':forms.NumberInput(attrs={'class':'form-control','id':'rental_price'}),
            'retal_period':forms.NumberInput(attrs={'class':'form-control','id':'rental_period'}),
            'total_rental':forms.NumberInput(attrs={'class':'form-control','id':'total_rental'}),
            'active':forms.Select(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'}),


           # 'name':forms.TextInput(attrs={'class':'form-control'})
            
        }




