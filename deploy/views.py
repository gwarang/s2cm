from django.shortcuts import render, redirect
from django.http import HttpResponse
from deploy.forms import DeployForm
import subprocess, os

def deploy(request):
    if request.method == "GET":
        return render(request, 'deploy/deploy.html')

    elif request.method == "POST":
        stack_name = ''
        stack_name = request.POST.get('stack_name') #deployForm.cleaned_data['stack_name']
        yml = request.POST.get('create_yml') # deployForm.cleaned_data['create_yml']

        deploy_data_path = os.getcwd() + '/deploy_data'
        yml_dir_path = os.getcwd() + '/dir_yml' 
        yml_path = yml_dir_path + '/temp.yml'
    
        with open(yml_path, 'w') as f:
            f.write(yml)

        sh_path = deploy_data_path + '/deploy.sh'
        
        if stack_name != '':
            command = sh_path + ' ' + yml_path + ' ' + stack_name
            ret = subprocess.run(command, shell=True, check=True)
        else:
            command = 'stack name or yml file is wrong'
        return redirect('/stacks/' + stack_name)
    #return HttpResponse(command)
