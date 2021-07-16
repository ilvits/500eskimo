from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Icecream
from .forms import IcecreamForm


def index(request):
	return render(request, 'order/index.html')
	

def order(request):
	icecreams = Icecream.objects.order_by('name')
	context = {'icecreams' : icecreams}
	return render(request, 'order/order.html', context)

@login_required
def new_icecream(request):
	"""Добавляем новое мороженое"""
	if request.method != 'POST':
		# Данные не отправлялись. Делаем пустую форму
		form = IcecreamForm()
	else:
		# Данные POST отправлены. Обрабатываем форму
		form = IcecreamForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('order:order')
	# Вывести пустую или недейсвительную форму.
	context = {'form': form}
	return render(request, 'order/new_icecream.html', context)
