from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView
from .models import Trip
from .forms import TripForm

class TripListView(ListView):
    model = Trip
    template_name = 'trips/trip_list.html'  # Убедитесь, что этот шаблон существует
    context_object_name = 'trips'  # Имя переменной, доступной в шаблоне

class TripCreateView(CreateView):
    model = Trip
    form_class = TripForm
    template_name = 'trips/trip_form.html'  # Создайте этот шаблон для формы
    success_url = '/trips/'  # URL для перенаправления после успешного создания

def trip_detail(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)  # Получите путешествие по ID или 404, если не найдено
    return render(request, 'trips/trip_detail.html', {'trip': trip})  # Передайте детали путешествия в шаблон

def trip_list(request):
    trips = Trip.objects.all()  # Получите все путешествия из базы данных
    return render(request, 'trips/trip_list.html', {'trips': trips})  # Передайте список путешествий в шаблон

def trip_create(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраните объект путешествия в базе данных
            return redirect('trip_list')  # Перенаправление на список путешествий после успешного создания
    else:
        form = TripForm()  # Если метод GET, создайте пустую форму

    return render(request, 'trips/trip_form.html', {'form': form})  # Обратите внимание на правильный шаблон
