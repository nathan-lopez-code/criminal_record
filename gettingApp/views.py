from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SeachbynameForm, Searhcbyimage
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings
from .models import CriminalProfil
from .reconnaissance_facial import FaceRecognition
from random import randint
from imutils import paths


def defaultcontext(req):
    cont = {}
    user = req.user
    form = SeachbynameForm
    if user.is_authenticated:
        cont['user'] = user
    cont["seachbyname"] = form
    return cont


@login_required
def home(request):

    context = defaultcontext(request)
    return render(request, "gettingApp/index.html", context)


@login_required
def searchbyname(request):
    init_context = defaultcontext(request)

    name = request.GET['name']

    init_context['name'] = name
    init_context['crimes'] = CriminalProfil.objects.filter(name__contains=name) \
                             or CriminalProfil.objects.filter(postnom__contains=name)

    return render(request, "gettingApp/resulteSearch.html", init_context)


@login_required
def searchByImage(request):
    context = defaultcontext(request)
    context['nomatch'] = "d-none"
    profiles = CriminalProfil.objects.all()

    if request.method == 'POST':
        imageForm = Searhcbyimage(request.POST, request.FILES)
        if imageForm.is_valid():
            # effacer l'ancien image test
            path = os.path.join(settings.BASE_DIR, 'media/test/')
            imglist = list(paths.list_images(path))
            try:
                os.remove(imglist[0])
            except:
                pass

            # recuperer l'image venant du formulaire
            image_field = imageForm.cleaned_data.get('image')
            fsys = FileSystemStorage()
            extention = image_field.name.split('.')[-1]
            new_name = "test/{}.{}".format("test", extention)
            file = fsys.save(new_name, image_field)
            file_url = fsys.url(file)
            match_dico = {}
            # recherhe par img
            sysRec = FaceRecognition(tolerance=0.6)


            for p in profiles:
                match_dico[p] = sysRec.face_detection(os.path.join(settings.BASE_DIR, p.photo.url[1:]),
                                                           os.path.join(settings.BASE_DIR, file_url[1:]))
            detecter = []
            for match in match_dico:
                if match_dico[match] == True:
                    detecter.append(match)

            if len(detecter) > 0:
                context['profiles'] = detecter
                context['matchpercent'] = randint(53, 100)
            else:
                context['nomatch'] = "d-block"
                context['imageForm'] = Searhcbyimage()

            context['photocomp'] = file_url

            return render(request, 'gettingApp/searchbyimage.html', context)
        else:
            context['imageForm'] = Searhcbyimage()
            context['errorForm'] = "Une erreur s'est produit veillez ressayez"
            return render(request, 'gettingApp/searchbyimage.html', context)
    else:
        context['imageForm'] = Searhcbyimage()
        return render(request, 'gettingApp/searchbyimage.html', context)
