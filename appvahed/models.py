# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class mdl_sakhtemoun(models.Model):
    name=models.CharField(max_length=128,verbose_name="نام")

    def __unicode__(self):
        return self.name
		
		
		
		
class mdl_vahed(models.Model):
    sakhtemoun=models.ForeignKey(mdl_sakhtemoun,verbose_name="نام ساختمان")
    name=models.CharField(max_length=128,verbose_name="نام")
    lname=models.CharField(max_length=128,verbose_name="نام خانوادگی")
    metraj=models.CharField(max_length=128,verbose_name="متراژ")
    def __unicode__(self):
        return self.name