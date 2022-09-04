from django.shortcuts import redirect
import os, subprocess

def rollback(request, service_name):
    command = 'docker service rollback ' + service_name
    ret = subprocess.run(command, shell=True, check=True)

    return redirect('/services/')
 

