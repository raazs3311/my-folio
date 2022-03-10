
from django.shortcuts import render

from .form import ContactForm
from .models import Images

# Create your views here.


def base(request):
    return render(request, 'base.html')
    

def raaz(request):
    var1 = Images.objects.all()
    
    
    form = ContactForm(request.POST)
    if  request.method == 'POST':
        if form.is_valid():

         form.save()
    return render(request, 'raaz.html', {'form':form, 'var1':var1})

def contact(request):
    fom = ContactForm(request.POST)
    if  request.method == 'POST':
        if fom.is_valid():

         fom.save()
    return render(request, 'contact.html',{'fom':fom} )