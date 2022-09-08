from django.shortcuts import render
from django.http import FileResponse
from gettingApp.models import CriminalProfil, Crime
from django.views.generic import DetailView
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from gettingApp.views import defaultcontext, SeachbynameForm
import os.path
import io
from imutils import paths
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


class DetailCasier(LoginRequiredMixin, DetailView):
    context_object_name = "profile"
    model = CriminalProfil
    template_name = "settingApp/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['crimes'] = self.object.crime_set.all()
        context['seachbyname'] = SeachbynameForm
        return context


@login_required
def affichage_(request):
    context = defaultcontext(request)
    crimes = CriminalProfil.objects.all()

    context['crimes'] = crimes
    return render(request, "settingApp/screen.html", context)


@login_required
def downloadfile(request, pk):
    profile = CriminalProfil.objects.get(pk=pk)
    photo = profile.photo.url
    nomc = (profile.name + " " + profile.postnom + " " + profile.prenom).upper()
    genre = []

    if profile.genre == "M":
        genre.append("le nommé")
        genre.append("fils de ")

    else:
        genre.append("la nommée")
        genre.append("fille de")

    imgpath = os.path.join(settings.BASE_DIR, "static/img/others/")
    imglist = list(paths.list_images(imgpath))

    buffer = io.BytesIO()
    canva = canvas.Canvas(buffer, pagesize=A4)
    canva.setLineWidth(.3)
    canva.setFont('Helvetica', 12)
    canva.drawString(10, 800, 'REPUBLIQUE DEMOCRATIQUE DU CONGO')
    canva.setFont('Helvetica', 11)
    canva.drawString(20, 785, "ministere de la justice et droit de l'homme")
    canva.drawImage(imglist[1], 50, 635, width=150,  preserveAspectRatio=True, mask='auto')
    canva.setFont('Helvetica-Bold', 12)
    canva.drawString(260, 640, "BULTIN N°3")
    canva.drawString(210, 625, "EXTRAIT DU CASIER JUDICIAIRE")
    my_Style = ParagraphStyle('My Para style',
                              fontName='Times-Roman',
                              backColor='#FFFFFF',
                              fontSize=12,
                              leading=20,
                              alignment=0
                              )

    p1 = Paragraph('''Relevé des condamnation à des peines privatives de liberté concernant<BR/> {}
    <u><b> {} </b></u> <BR/>'''.
                   format(genre[0], nomc, ), my_Style)
    p1.wrapOn(canva, 500, 50)
    p1.drawOn(canva, 50, 485)
    p2 = Paragraph('''{} <u>{}</u> <br/> et de <u>{}</u>'''.format(genre[1], profile.nom_pere.upper(), profile.nom_mere.upper()), my_Style)
    p2.wrapOn(canva, 500, 50)
    p2.drawOn(canva, 70, 445)
    p3 = Paragraph(''' né le <u>{}</u> à <u>{}</u> <br/> Domicile : <u>{}</u> <br/> Etat civil : <u>{}</u> <br/>
     Nationalité : <u>{}</u> <br/> Profession : <u>{}</u>'''
                   .format(profile.date, profile.lieu, profile.adresse, profile.etatcivile, profile.nationalite,
                           profile.profession), my_Style)
    p3.wrapOn(canva, 500, 50)
    p3.drawOn(canva, 50, 390)
    canva.showPage()
    canva.save()

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='extrait du casier de {}.pdf'.format(profile.name))

@login_required
def downloadpreview_(request):
    context = defaultcontext(request)
    crimes = CriminalProfil.objects.all()

    context['crimes'] = crimes
    return render(request, "settingApp/downloadExtrait.html", context)


@login_required
def about_us(request):
    context = defaultcontext(request)

    return render(request, 'settingApp/apropos.html', context)
