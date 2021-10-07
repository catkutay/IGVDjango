from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . models import Disease
from . forms import *
def home(request):
	data = Disease.objects.all()
	return render(request, 'home.html', {'data': data,'active': ""})

def recipe(request,id):
	print(id)
	try:
		disease=Disease.objects.get(id=id)
		data = Recipies.objects.get(disease=disease)
	except Exception:
		return render(request, 'empty.html')

	print(data)

	return render(request, 'recipe.html', {'data': data, 'active': disease.name})



'''if request.method == 'POST':
		form = recipieForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
	else:
		form=recipieForm()'''