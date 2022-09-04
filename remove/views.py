from django.shortcuts import render, redirect
import os, subprocess

def remove(requests, stack_name):
    remove_path = os.getcwd() + '/command_sh/stack_remove.sh'
    command = remove_path + ' ' + stack_name

    ret = subprocess.run(command, shell=True, check=True)
    return redirect('/stacks/')
    #return HttpResponse('remove')
