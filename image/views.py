from django.shortcuts import render, redirect
import os

def image_push(request):
    if request.method == "GET":

        return render(request, 'image/image_push.html')

    # form으로 입력받은 데이터 저장/배포
    elif request.method == "POST":

        imagename = request.POST.get('imagename') 
        tagname = request.POST.get('tagname')

        tag_ins_comm = 'docker tag ' + imagename +' localhost:5000/' +tagname
        tag_stream = os.popen(tag_ins_comm)
        tag_stream_output = tag_stream.read()

        push_comm = 'docker push localhost:5000/'+tagname
        push_stream = os.popen(push_comm)
        push_stream_output = push_stream.read()

        return redirect('/images/')

def image_pull(request):
    if request.method == "GET":
        return render(request, 'image/image_pull.html')
    elif request.method == "POST":
        imageurl = request.POST.get('imageurl')
        imagename = request.POST.get('imagename')
        mkimg_ins_comm=""
        if imageurl == "":
            mkimg_ins_comm = 'docker image pull ' + imagename
        else:
            mkimg_ins_comm = 'docker pull ' + imageurl+'/'+imagename
        img_stream = os.popen(mkimg_ins_comm)
        img_stream_output = img_stream.read()
        return redirect('/images/')


def image_list(request):
    command = 'docker image ls --format "{{.Repository}}\t{{.Tag}}\t{{.ID}}\t{{.CreatedAt}}\t{{.Size}}"'
    stream = os.popen(command)
    output = stream.read()
    lines = output.split('\n')

    infos = []
    for line in lines:
        if len(line) == 0:
            continue
        temp = line.split('\t')
        if '/' in  temp[0]:
            temp[0] = temp[0].replace('/', '_|')
        infos.append(temp)

    context = {
            'infos':infos,
            }

    return render(request, 'image/image_lists.html',context)


def image_create(request):
    if request.method == "GET":
        return render(request, 'image/create.html')
    elif request.method == "POST":
        image_name = request.POST.get('image_name')
        dockerfile = request.POST.get('dockerfile')
        
        dockerfile_path = os.getcwd() + '/image_dockerfile/'
        with open(dockerfile_path + 'Dockerfile', 'w') as f:
            f.write(dockerfile)
        
        command = 'docker build -t ' + image_name + ' ' + dockerfile_path
        stream = os.popen(command)
        output = stream.read()
        return redirect('/images/')


def image_remove(request, image_name, image_tag):
    if '_|' in image_name:
        image_name = image_name.replace('_|', '/')
    command = 'docker image rm ' + image_name + ':' + image_tag
    stream = os.popen(command)
    output = stream.read()
    return redirect('/images/')

def image_inspect(request, image_name, image_tag):
    if '_|' in image_name:
        image_name = image_name.replace('_|', '/')

    command = 'docker image inspect ' + image_name + ':' + image_tag
    stream = os.popen(command)
    output = stream.read()
    context = { 'image_name': image_name, 'output' : output }
    return render(request, 'image/image_info.html', context)
