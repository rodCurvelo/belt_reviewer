# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib import messages
from .models import User

def flash_errors(errors, request):
	for error in errors:
		messages.error(request, error)

def current_user(request):
	return User.objects.get(id = request.session['user_id'])

def index(request):
	return render(request, 'login_registration/index.html')

def success(request):
	if 'user_id' in request.session:
		context = {
			'user': current_user(request),
		}

		return render(request, 'login_registration/success.html', context)

	return redirect(reverse('landing'))

def register(request):
	if request.method == "POST":
		# validate form data
		errors = User.objects.validate_registration(request.POST)
		
		# Check if errors don't exist
		if not errors:
			# create user 
			user = User.objects.create_user(request.POST)

			# log in the user
			request.session['user_id'] = user.id

			# redirect to success page
			return redirect(reverse('dashboard'))

		# flash errors
		flash_errors(errors, request)

	# redirect landing 
	return redirect(reverse('landing'))

def login(request):
	if request.method == "POST":
		# Validate my login data
		check = User.objects.validate_login(request.POST)

		# Check if retrived a valid user
		if check['user']:
			# log in my user
			request.session['user_id'] = check['user'].id

			# redirect to success page
			return redirect(reverse('dashboard'))

		# Flash error messages	
		flash_errors(check['errors'], request)

	return redirect(reverse('landing'))

def logout(request):
	if 'user_id' in request.session:
		request.session.pop('user_id')

	return redirect(reverse('landing'))


