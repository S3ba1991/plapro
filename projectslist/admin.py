# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Author, DesignerList, Project

# Register your models here.

admin.site.register([Author, DesignerList, Project])