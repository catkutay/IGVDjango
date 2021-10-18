from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template.defaulttags import csrf_token

from .models import Disease
from .models import Recipies
from .forms import *


def home(request):
    data = Disease.objects.all()
    return render(request, 'home.html', {'data': data, 'active': ""})


def recipe(request, id):
    print(id)
    try:
        disease = Disease.objects.get(id=id)
        data = Recipies.objects.get(disease=disease)
    except Exception:
        return render(request, 'empty.html')

    print(data)

    return render(request, 'recipe.html', {'data': data, 'active': disease.name})


def upload(request, id):
    if request.method == 'POST':
        disease = Disease.objects.get(id=id)
        form = RecipeForm()
        try:
            Recipies.objects.filter(disease=disease).delete()
        except:
            pass

        name = request.POST['name']
        audio = request.POST['audio']
        print(audio)
        image1 = request.FILES['image1']
        desc1 = request.POST['desc1']
        image2 = request.FILES['image2']
        desc2 = request.POST['desc2']
        image3 = request.FILES['image3']
        desc3 = request.POST['desc3']
        image4 = request.FILES['image4']
        desc4 = request.POST['desc4']
        ins = Recipies(name=name, audio=audio, disease=disease, image1=image1, description1=desc1, image2=image2, description2=desc2,
                       image3=image3, description3=desc3, image4=image4, description4=desc4
                       )
        ins.save()
        print(name, image1, desc1)

    else:
        form = RecipeForm()
    return render(request, 'upload.html', {'form': form})
