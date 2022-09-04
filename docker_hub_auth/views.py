from django.shortcuts import render, redirect
from django.http import HttpResponse
from docker_hub_auth.forms import LoginForm
import subprocess

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        print('login POST')
        ids = request.POST.get('docker_id')
        print(type(ids))
        print(ids)
        pws = request.POST.get('docker_pw')
        print(type(pws))
        print(pws)
        command = 'docker login --username ' + ids + ' --password ' + pws
        ret = subprocess.run(command, shell=True, check=True)
        return redirect('/main/')


def logout(request):
    return HttpResponse('logout')
