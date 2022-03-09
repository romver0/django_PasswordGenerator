import random

from django.shortcuts import render
# from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    color_list=['Salmon','pink','MediumSpringGreen','BurlyWood','BurlyWood','Azure','cyan','MediumPurple','CornflowerBlue']
    color=random.choice(color_list)
    return render(request, 'generator/home.html',{'color':color})
    # return HttpResponse("Это страница home")

def password(request):
    color_list=['alert alert-primary','alert alert-secondary','alert alert-success','alert alert-danger','alert alert-warning',
                'alert alert-info','alert alert-dark']
    color = random.choice(color_list)
    characters=list('abcdefghijklmnopqrstuvwxyz')
    characters_upper=list('abcdefghijklmnopqrstuvwxyz'.upper())
    characters_number=list('0123456789')
    characters_special=list('~!@#$%^&*()-+)')

    if request.GET.get('uppercase'):
        characters.extend(characters_upper)
    if request.GET.get('numbers'):
        characters.extend(characters_number)
    if request.GET.get('special'):
        characters.extend(characters_special)
    default=5
    length=int(request.GET.get('length',default))
    thepassword=''
    for x in range(length):
        # if request.GET.get('uppercase'):
        #     thepassword+=random.choice(characters_upper)
        # if request.GET.get('numbers'):
        #     thepassword += random.choice(characters_number)
        # if request.GET.get('special'):
        #     thepassword += random.choice(characters_special)
        thepassword+=random.choice(characters)
    return render(request,'generator/password.html',{'password':thepassword,'color':color})

def description(request):
    return render(request,'generator/description.html')