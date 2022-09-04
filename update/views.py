from django.shortcuts import render, redirect
from django.http import HttpResponse
from update.forms import UpdateForm
import docker


def update(request, service_name):
    if request.method == "GET":
        return render(request, 'update/update.html')
    elif request.method == "POST":
        
        client = docker.from_env()
        
        image_name = request.POST.get('update_image_name')  #updateForm.cleaned_data['update_image_name']
        print(image_name) 
        service = client.services.get(service_name)
        service.update(image=image_name)

    return redirect('/services/') 
