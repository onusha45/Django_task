from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def index(request):
    folders = Folder.objects.all()

    # Get Parent of All Sub Folders
    print("\n--------------Parents------------")
    for folder in folders:
        print(folder.get_parent)

    # Get SubFolders of Parents
    # print("-----------Childerns-------------")
    # for folder in folders:
    #     print(folder.get_children)

    context = {
            'folders' : folders
        }

    return render(request, 'folders.html', context)


def get_subfolders(request, id):

    parent = Folder.objects.get(id=id)
    subfolders = parent.get_children

    return render(request, 'subfolders.html', {'subfolders' : subfolders})
    
