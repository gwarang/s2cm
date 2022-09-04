from django.shortcuts import redirect
import docker

def scale(request):
    client = docker.from_env()
    service_name = request.GET.get('service_name')
    service = client.services.get(service_name)
    scale_num = int(request.GET.get('scale_num'))

    service.scale(scale_num)


    return redirect('/services/')
