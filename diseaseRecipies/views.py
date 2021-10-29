from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template.defaulttags import csrf_token
from django.db import models
from .models import Disease
from .models import Recipies
from .models import *
from .forms import *

from django.core.files import File


def home(request):
    data = Disease.objects.all()
    return render(request, 'home.html', {'data': data, 'active': ""})


def recipe(request, id):
    print(id)
    image_urls = []
    audio_urls = []
    desc_list = []
    try:
        disease = Disease.objects.get(id=id)
        data = Recipies.objects.get(disease=disease)
        dataAll = fetchData(data)

    except Exception as e:
        print(e)
        return render(request, 'empty.html')

    print(data)
    d1 = [{'data': 'akash'}, {'data': 'goyal'}]
    return render(request, 'recipe.html',
                  {'data': data, 'dataAll': dataAll, 'images': image_urls, 'audios': audio_urls, 'desc': desc_list,
                   'active': disease.name})


def upload(request, id):
    if request.method == 'POST':
        disease = Disease.objects.get(id=id)
        form = RecipeForm()
        try:
            Recipies.objects.filter(disease=disease).delete()
        except:
            pass
        audios = []
        images = []
        name = request.POST['name']
        for i in range(1, 5):
            try:
                audios.append(request.FILES['audio' + str(i)])
                print(audios)
                print(type(audios[0]))
            except:
                audios.append("")
            try:
                images.append(request.FILES['image' + str(i)])
            except:
                images.append("")

        desc1 = request.POST['desc1']
        if (desc1 != ""):
            textToSpeech(desc1, 'desc1.mp3')
        desc2 = request.POST['desc2']
        if (desc2 != ""):
            textToSpeech(desc2, 'desc2.mp3')
        desc3 = request.POST['desc3']
        if (desc3 != ""):
            textToSpeech(desc3, 'desc3.mp3')
        desc4 = request.POST['desc4']
        if (desc4 != ""):
            textToSpeech(desc4, 'desc4.mp3')
        print(audios)

        '''ins = Recipies(name=name, audio1=audios[0], disease=disease, image1=images[0], description1=desc1,
                           image2=images[1],
                           description2=desc2, audio2=audios[1], image3=images[2], description3=desc3, audio3=audios[2],
                           image4=images[3], description4=desc4,
                           audio4=audios[3])'''
        ins = Recipies(name=name, disease=disease, audio1=audios[0], image1=images[0], description1=desc1,
                       image2=images[1],
                       description2=desc2, audio2=audios[1], image3=images[2], description3=desc3, audio3=audios[2],
                       image4=images[3], description4=desc4,
                       audio4=audios[3])

        with open("desc1.mp3", "rb") as aud:
            ins.audioDesc1.save(str(id) + "desc1.mp3", aud)
        with open("desc2.mp3", "rb") as aud:
            ins.audioDesc2.save(str(id) + "desc2.mp3", aud)
        with open("desc3.mp3", "rb") as aud:
            ins.audioDesc3.save(str(id) + "desc3.mp3", aud)
        with open("desc4.mp3", "rb") as aud:
            ins.audioDesc4.save(str(id) + "desc4.mp3", aud)

        ins.save()


    else:
        form = RecipeForm()
    return render(request, 'upload.html', {'form': form})


def fetchData(data):
    urls = []
    if data.image1 != "":
        dic = {}
        dic['image'] = data.image1.url
        if data.audio1 != "":
            dic['audio'] = data.audio1.url
        dic['desc'] = data.description1
        dic['audioDesc'] = data.audioDesc1.url
        dic['id'] = "1"
        urls.append(dic)
    if data.image2 != "":
        dic = {}
        dic['image'] = data.image2.url
        if data.audio1 != "":
            dic['audio'] = data.audio2.url
        dic['desc'] = data.description2
        dic['audioDesc'] = data.audioDesc2.url
        dic['id'] = "2"
        urls.append(dic)
    if data.image3 != "":
        dic = {}
        dic['image'] = data.image3.url
        if data.audio1 != "":
            dic['audio'] = data.audio3.url
        dic['desc'] = data.description3
        dic['audioDesc'] = data.audioDesc3.url
        dic['id'] = "4"
        urls.append(dic)
    if data.image4 != "":
        dic = {}
        dic['image'] = data.image3.url
        if data.audio1 != "":
            dic['audio'] = data.audio3.url
        dic['desc'] = data.description4
        dic['audioDesc'] = data.audioDesc4.url
        dic['id'] = "4"
        urls.append(dic)
    return urls


def textToSpeech(desc, name):
    from gtts import gTTS

    # This module is imported so that we can
    # play the converted audio
    import os

    # The text that you want to convert to audio

    # Language in which you want to convert
    language = 'en'

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    myobj = gTTS(text=desc, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome
    myobj.save(name)
    return myobj
    # Playing the converted file
    # os.system("mpg321 welcome.mp3")
