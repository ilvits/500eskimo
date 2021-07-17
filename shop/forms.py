
from django import forms
from .models import Icecream

class IcecreamForm(forms.ModelForm):
	class Meta:
		model = Icecream
		fields = ['name', 'description', 'image', 'active', 'category', 'price']
		labels = {'name': 'Название', 'description': 'Описание', 'image': 'Изображение', 'active': 'Активировать', 'category': 'Категория', 'price': 'Цена за шт.'}
		widgets = {'description': forms.Textarea(attrs={'cols': 80})}
