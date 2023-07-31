from django.shortcuts import render
from main.models import *
from django.http import HttpResponse
import os
from django import forms
from django.http import FileResponse, HttpResponse
from django.shortcuts import render

from django import forms
from paiement.forms import ComptableForm, FicheDePaieForm, PaiementForm

import datetime
from main.pdfMaker import generate_pdf
from django.shortcuts import get_object_or_404, redirect, render




def create_comptable(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = ComptableForm()
        else:
            comptable = Comptable.objects.get(pk=id)
            form = ComptableForm(instance=comptable)
        return render(request, 'comptables/create_comptable.html', {'form': form})
    else:
        if id == 0:
            form = ComptableForm(request.POST)
        else:
            comptable = Comptable.objects.get(pk=id)
            form = ComptableForm(request.POST, instance=comptable)
        if form.is_valid():
            exit
            form.save()
            return redirect('/paiement/comptable_list')
        else:
            return render(request, 'comptables/create_comptable.html', {'form': form})
    


def comptable_detail(request, id):
    comptable = get_object_or_404(Comptable, id=id)
    return render(request, 'comptables/comptable_detail.html', {'comptable': comptable})


def edit_comptable(request, id):
    comptable = Comptable.objects.get(id=id)
    
    if request.method == 'POST':
        form = ComptableForm(request.POST, request.FILES, instance=comptable)
        if form.is_valid():
            comptable = form.save(commit=False)
            comptable.save()
            return redirect('/paiement/comptable_list')
    else:
        form = ComptableForm(instance=comptable)
    
    return render(request, 'comptables/edit_comptable.html', {'form': form})


def comptable_list(request):
    comptables = Comptable.objects.all()
    return render(request, 'comptables/comptable_list.html', {'comptables': comptables})


def paiement_list(request):
    paiements = Paiement.objects.all()
    return render(request, 'paiements/paiement_list.html', {'paiements': paiements})

def paiement_detail(request, id):
    paiement = Paiement.objects.get(id=id)
    return render(request, 'paiements/paiement_detail.html', {'paiement': paiement})

def create_paiement(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = PaiementForm()
        else:
            paiement = Paiement.objects.get(pk=id)
            form = PaiementForm(instance=paiement)
        return render(request, "paiements/create_paiement.html", {'form': form})
    else:
        if id == 0:
            form = PaiementForm(request.POST)
        else:
            paiement = Paiement.objects.get(pk=id)
            form = PaiementForm(request.POST, instance=paiement)
        if form.is_valid():
            form.save()
            return redirect('/paiement/paiement_list')
        else:
            print(form.errors)
            return render(request, "paiements/create_paiement.html", {'form': form})

def edit_paiement(request, id):
    paiement = Paiement.objects.get(id=id)
    if request.method == 'POST':
        form = PaiementForm(request.POST, instance=paiement)
        if form.is_valid():
            form.save()
            return redirect('/paiement/paiement_list')
    else:
        form = PaiementForm(instance=paiement)
        form.fields['montant'].initial = 0  # Définir la valeur par défaut à zéro
    return render(request, 'paiements/edit_paiement.html', {'form': form})


def fiche_de_paie_list(request):
    fiches = FicheDePaie.objects.all()
    return render(request, 'fichePaies/fiche_de_paie_list.html', {'fiches': fiches})

def fiche_de_paie_detail(request, id):
    fiche_de_paie = get_object_or_404(FicheDePaie, id=id)
    return render(request, 'fichePaies/fiche_de_paie_detail.html', {'fiche_de_paie': fiche_de_paie})

def create_fiche_de_paie(request):
    if request.method == "POST":
        form = FicheDePaieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/paiement/fiche_de_paie_list')
    else:
        form = FicheDePaieForm()

    return render(request, 'fichePaies/create_fiche_de_paie.html', {'form': form})

def update_fiche_de_paie(request, id):
    fiche_de_paie = get_object_or_404(FicheDePaie, id=id)

    if request.method == "POST":
        form = FicheDePaieForm(request.POST, instance=fiche_de_paie)
        if form.is_valid():
            form.save()
            return redirect('/paiement/fiche_de_paie_list')
    else:
        form = FicheDePaieForm(instance=fiche_de_paie)

    return render(request, 'fichePaies/update_fiche_de_paie.html', {'form': form})



def fiche_paie(request, id):
    fiche_paie = get_object_or_404(FicheDePaie, id=id)
    context = {'fiche_paie': fiche_paie}

    # nom des fichiers d'entrée et de sortie
    latex_input = 'fiche_paie'
    latex_ouput = 'generated_fiche_paie'
    pdf_file = 'pdf_fiche_paie'

    # génération du pdf
    generate_pdf(context, latex_input, latex_ouput, pdf_file)

    #visualisation du pdf dans le navigateur
    with open('media/pdf/' + str(pdf_file) + '.pdf', 'rb') as f:
        pdf_preview = f.read()
        response = HttpResponse(pdf_preview, content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=pdf_file.pdf'
        return response