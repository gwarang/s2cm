from django.shortcuts import render
import os

def main_page(request):

    command = 'docker node ls'
    stream = os.popen(command)
    output = stream.read()

    lines = output.split('\n')
    nodes = []
    hostnames = []
    for line in lines:
        if 'NAME' in line: continue
        elif len(line) == 0: continue
        else:
            if '*' not in line:
                temp = list(line.split())
                if len(temp) == 6:
                    nodes.append(temp)
                    hostnames.append(temp[1])
                else:
                    temp.insert(-1, ' ')
                    nodes.append(temp)
                    hostnames.append(temp[1])
            else:
                temp = list(line.split())
                temp[0] += ' *'
                temp.pop(1)
                nodes.append(temp)
                hostnames.append(temp[1])

    cpu_usages = []
    for hostname in hostnames:
        if hostname == 'manager':
            command = "sar 1 1 | grep Average | gawk '{{print $8}}'"
        else:
            command = "ssh root@" + hostname + " sar 1 1 | grep Average | gawk '{{print $8}}'"
        stream = os.popen(command)
        output = stream.read()

        cpu_usages.append((hostname, 100.0 - float(output)))

    context = { 'nodes' : nodes, 'cpu_usages' : cpu_usages, }

    

    return render(request, 'index.html', context)


def node_info(request, node_name):
    command = 'docker node inspect ' + node_name + ' --pretty'
    stream = os.popen(command)
    output = stream.read()
    return render(request, 'main/node_info.html', {'node_name': node_name, 'output': output})


