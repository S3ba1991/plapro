# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import ListView, DetailView


from models import Author

class AuthorListView(ListView):
    model = Author

class AuthorDetailView(DetailView):
    model = Author