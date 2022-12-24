from distutils.command.build_scripts import first_line_re
from django.shortcuts import redirect, render
from .models import Song
from django.contrib import messages

from django import forms
from django.http import HttpResponse
from cloudinary.forms import cl_init_js_callbacks
from .forms import PhotoForm

def index(request):

    photo = Song.objects.all()
    print(photo)
    # adding context 
    ctx = {'photo':photo}
    return render(request, 'index.html', ctx)


def Upload(request):
    context = dict(backend_form = PhotoForm())
    if request.method == "POST":
        form = PhotoForm(request.POST,request.FILES)
        context['posted'] = form.instance
        print('____________________________')
        print(form)
        print('____________________________')
        print(context)
        print('____________________________')

        if form.is_valid():
            form.save()
            return redirect('/')
    form = PhotoForm()
    ctx = {'form': form}
    return render(request,'upload.html',ctx)