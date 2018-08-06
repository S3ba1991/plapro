# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Author(models.Model):
    firstName = models.CharField(max_length=15)
    lastName = models.CharField(max_length=15)


class DesignerList(models.Model):
    list = models.CharField(max_length=15)


class Project(models.Model):
    author = models.ForeignKey(Author)
    designerList = models.ForeignKey(DesignerList)
    title = models.CharField(max_length=100)
    startDate = models.DateField()
    endDate = models.DateField()
    status = models.CharField(max_length=1)
