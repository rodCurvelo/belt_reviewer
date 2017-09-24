# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse

# Create your views here.
def index(request):
	return render(request, 'review_app/index.html')