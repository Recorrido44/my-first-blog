# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from forms import ParametroForm, PostForm, ViajeForm
from django.utils import timezone
from gestion_viaje.models import Parametro, Kilometro


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.valido = 'T'
            post.fecha = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Parametro, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.valido = 'T'
            post.fecha = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Parametro, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def viaje_new(request):
    if request.method == "POST":
        form = ViajeForm(request.POST)
        if form.is_valid():
            viaje = form.save(commit=False)
            viaje.kmfin = 0
            viaje.fechaini = timezone.now()
            viaje.fechafin = timezone.now()
            viaje.entrada = 0
            viaje.save()
            return redirect('viaje_detail', pk=viaje.pk)
    else:
        form = ViajeForm()
    return render(request, 'viaje_edit.html', {'form': form})

def viaje_edit(request, pk):
    post = get_object_or_404(Kilometro, pk=pk)
    if request.method == "POST":
        form = ViajeForm(request.POST, instance=post)
        if form.is_valid():
            viaje = form.save(commit=False)
            viaje.valido = 'T'
            viaje.fecha = timezone.now()
            viaje.save()
            return redirect('viaje_detail', pk=post.pk)
    else:
        form = ViajeForm(instance=post)
    return render(request, 'viaje_edit.html', {'form': form})

def viaje_detail(request, pk):
    viaje = get_object_or_404(Kilometro, pk=pk)
    return render(request, 'viaje_detail.html', {'viaje': viaje})
