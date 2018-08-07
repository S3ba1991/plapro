# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Author(models.Model):
    firstName = models.CharField(max_length=15)
    lastName = models.CharField(max_length=15)

    def __str__(self):
        return "{fN} {lN}".format(fN=self.firstName, lN=self.lastName)


class Designer(models.Model):
    firstName = models.CharField(max_length=15)
    lastName = models.CharField(max_length=15)

    def __str__(self):
        return "{fN} {lN}".format(fN=self.firstName, lN=self.lastName)


class Project(models.Model):
    author = models.ForeignKey(Author)
    designerList = models.ManyToManyField(Designer)
    title = models.CharField(max_length=100)
    startDate = models.DateField()
    endDate = models.DateField()
    statuses = (
        ('N', 'New'),
        ('R', 'In implementation'),
        ('D', 'Done'),
    )
    status = models.CharField(max_length=1, choices=statuses, default='N')
    content = models.CharField(max_length=5000, default='')

    def __str__(self):
        return self.title
