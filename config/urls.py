"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import deploy.views
import remove.views
import update.views
import rollback.views
import dockerList.views
import scale.views
import network.views
import volume.views
import main.views
import docker_hub_auth.views
import image.views

urlpatterns = [
    path('', main.views.main_page),
    path('main/', main.views.main_page),
    path('admin/', admin.site.urls),

    path('node/<str:node_name>/', main.views.node_info),

    path('deploy/', deploy.views.deploy),
    path('stacks/remove/<str:stack_name>/', remove.views.remove),
    path('services/update/<str:service_name>', update.views.update),
    path('services/rollback/<str:service_name>', rollback.views.rollback),

    path('stacks/', dockerList.views.stack_list),
    path('stacks/<str:stack_name>/', dockerList.views.stack_info),
    path('services/', dockerList.views.service_list),
    path('services/scale/', scale.views.scale),
    path('services/<str:service_name>/', dockerList.views.service_info),


    path('network/', network.views.network_lists),
    path('network/create/', network.views.create),
    path('network/remove/<str:network_name>/', network.views.remove),
    path('network/<str:network_name>/', network.views.inspect),

    path('volume/', volume.views.volume_lists),
    path('volume/create/', volume.views.create),
    path('volume/remove/<str:volume_name>/', volume.views.remove),
    path('volume/<str:volume_name>/', volume.views.inspect),

    path('login/', docker_hub_auth.views.login),
    path('logout/', docker_hub_auth.views.logout),

    path('images/', image.views.image_list),
    path('images/create/', image.views.image_create),
    path('images/remove/<str:image_name>/<str:image_tag>/', image.views.image_remove),
    path('images/<str:image_name>/<str:image_tag>/', image.views.image_inspect),
]
