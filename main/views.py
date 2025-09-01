from django.shortcuts import render, redirect, get_object_or_404
from .models import Cat
from django.views.decorators.csrf import csrf_exempt

def home(request):
	return render(request, 'index.html')

def choose_cat(request):
	cats = Cat.objects.all()
	return render(request, 'main/choose_cat.html', {'cats': cats})

@csrf_exempt
def select_cat(request, cat_id):
	cat = get_object_or_404(Cat, id=cat_id)
	request.session['chosen_cat_id'] = cat.id
	return redirect('home')
