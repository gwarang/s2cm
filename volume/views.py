from django.shortcuts import render, redirect
from django.http import HttpResponse
import subprocess, os
from volume.forms import CreateForm, RemoveForm

def create(request):
    if request.method == "GET":
        return render(request, 'volume/create.html')

    elif request.method == "POST":
        vol_name = ''
        vol_name = request.POST.get('volume_name') #createForm.cleaned_data['volume_name']

        if vol_name != '':
            command = 'docker volume create ' + vol_name
            ret = subprocess.run(command, shell=True, check=True)
            return redirect('/volume/')


def volume_lists(request):
    command = 'docker volume ls'
    stream = os.popen(command)
    output = stream.read()

    lines = output.split('\n')
    volumes = []
    for line in lines:
        if 'NAME' in line: continue
        elif len(line) == 0: continue
        else:
            volumes.append(list(line.split()))

    return render(request, 'list/volume_tables.html', {'volumes': volumes,})


def inspect(request, volume_name):
    command = 'docker volume inspect '
    stream = os.popen(command)
    output = stream.read()

    createdAt = os.popen(command + "-f '{{ .CreatedAt }}' " + volume_name).read()
    driver = os.popen(command + "-f '{{ .Driver }}' " + volume_name).read()
    labels = os.popen(command + "-f '{{ .Labels }}' " + volume_name).read()
    mountpoint = os.popen(command + "-f '{{ .Mountpoint }}' " + volume_name).read()
    name = os.popen(command + "-f '{{ .Name }}' " + volume_name).read()
    options = os.popen(command + "-f '{{ .Options }}' " + volume_name).read()
    scope = os.popen(command + "-f '{{ .Scope }}' " + volume_name).read()

    context = {'CreatedAt' : createdAt, 'Driver' : driver, 'Labels' : labels, 'Mountpoint' : mountpoint, 'Name' : name, 'Options' : options, 'Scope' : scope, }

    return render(request, 'list/volume_info_tables.html', context)

def remove(request, volume_name):
    if volume_name != '':
        command = 'docker volume rm ' + volume_name
        ret = subprocess.run(command, shell=True, check=True)
    return redirect('/volume/')

