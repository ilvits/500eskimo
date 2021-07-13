from django.shortcuts import render
from .models import Icecream

def order(request):
	icecreams = Icecream.objects.order_by('name')
	context = {'icecreams' : icecreams}
	return render(request, 'order/order.html', context)