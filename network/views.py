from django.shortcuts import render, redirect
from django.http import HttpResponse
from network.forms import CreateForm, RemoveForm
import os, subprocess

def network_lists(request):
    command = 'docker network ls'
    stream = os.popen(command)
    output = stream.read()
    print(output)
    lines = output.split('\n')
    networks = []
    for line in lines:
        if 'NAME' in line: continue
        elif len(line) == 0: continue
        else:
            networks.append(list(line.split()))
    print(networks)

    return render(request, 'list/network_tables.html', {'networks': networks,})


def inspect(request, network_name):
    command = 'docker network inspect ' + network_name
    stream = os.popen(command)
    output = stream.read()
    return render(request, 'list/network_info.html', {'network_name':network_name, 'output':output})

def create(request):
    if request.method == "GET":
        return render(request, 'network/create.html')
    elif request.method == "POST":
        net_name = ''
        path = os.getcwd() + '/command_sh/network_create.sh'
        
        command = [path,]

            
        net_name = request.POST.get('network_name') # createForm.cleaned_data['network_name']
        if net_name != '': 
            command.append(request.POST.get('driver')) # createForm.cleaned_data['driver'])
            attachable = request.POST.get('attachable') # createForm.cleaned_data['attachable']
            if attachable:
                command.append('--attachable')

        if net_name == '':
            return HttpResponse('cannot create')
        else:
            command.append(net_name)
            ret = subprocess.run(' '.join(command), shell=True, check=True)
            return redirect('/network/' + net_name)

def remove(request, network_name):
    if network_name != '':
        command = 'docker network rm ' + network_name
        ret = subprocess.run(command, shell=True, check=True)
    return redirect('/network/')



