from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
	"""
	Регистрирует нового пользователя
	"""
	if request.method != 'POST':
		# Выводит пустую форму регистрации.
		form = UserCreationForm()
	else:
		# Обработка заполненной формы
		form = UserCreationForm(request.POST)

		if form.is_valid():
			new_user = form.save()
			# Выполнение входа и перенапраавление на дом. стр.
			login(request, new_user)
			return redirect('shop:catalog')
	# Вывести пустую или недействительную форму
	context = {'form': form}
	return render(request, 'registration/register.html', context)