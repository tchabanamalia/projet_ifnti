from django.shortcuts import render
from main.models import *
from django.http import HttpResponse
import os
from django import forms
from django.http import FileResponse, HttpResponse
from django.shortcuts import render

from django import forms
from paiement.forms import ComptableForm, PaiementForm

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


