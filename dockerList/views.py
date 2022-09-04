from django.shortcuts import render
from django.http import HttpResponse
import os


def stack_list(request): 

    stack_comm = 'docker stack ls'
    stack_stream = os.popen(stack_comm)
    stack_stream_output = stack_stream.read()

    lines = stack_stream_output.split('\n')
    stacks = []
    for line in lines:
        if 'NAME' in line: continue
        elif len(line) == 0: continue
        else:
            stacks.append(list(line.split()))
    return render(request, 'list/stack_tables.html', {'stacks': stacks,})


def service_list(request): 

    service_comm = 'docker service ls'
    service_stream = os.popen(service_comm)
    service_stream_output = service_stream.read()

    lines = service_stream_output.split('\n')
    services = []
    for line in lines:
        if 'NAME' in line: continue
        elif len(line) == 0: continue
        else:
            services.append(list(line.split()))
    print(services)

    return render(request, 'list/service_tables.html', {'services': services,})
    #return render(request, 'list/list.html', {'service_list': service_stream_output,})


def stack_info(request, stack_name):
    command = 'docker stack ps --format "{{.ID}}\t{{.Name}}\t{{.Image}}\t{{.Node}}\t{{.DesiredState}}\t{{.CurrentState}}\t{{.Error}}\t{{.Ports}}" ' + stack_name
    
    stream = os.popen(command)
    output = stream.read()
 
    lines = output.split('\n')
    stack_infos = []
    for line in lines:
        if len(line) == 0: continue
        else:
            stack_infos.append(list(line.split('\t')))
    return render(request, 'list/stack_info_tables.html', {'stack_infos': stack_infos,})



def service_info(request, service_name):
    command = 'docker service ps --format "{{.ID}}\t{{.Name}}\t{{.Image}}\t{{.Node}}\t{{.DesiredState}}\t{{.CurrentState}}\t{{.Error}}\t{{.Ports}}" ' + service_name
    
    stream = os.popen(command)
    output = stream.read()

    lines = output.split('\n')
    service_infos = []
    for line in lines:
        if 'NAME' in line: continue
        elif len(line) == 0: continue
        else:
            service_infos.append(list(line.split('\t')))
    return render(request, 'list/service_info_tables.html', {'service_infos': service_infos,})
