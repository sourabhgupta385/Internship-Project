# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class RssLinks(models.Model):
	provider = models.CharField(max_length = 30, default = None)
	category = models.CharField(max_length = 20 , default = None)
	link = models.CharField(max_length = 200)
