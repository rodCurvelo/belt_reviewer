# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, reverse
from ..login_registration.models import User
from ..review_app.models import Review
from django.contrib import messages
from .models import Book

def current_user(request):
	return User.objects.get(id=request.session['user_id'])

def flash_errors(request, errors):
	for error in errors:
		messages.error(request, error)

def index(request):
	return render(request, 'book_app/index.html')

def add(request):
	return render(request, 'book_app/add.html')

def create(request):
	if request.method == "POST":
		# Validate Form Data
		errors = Book.objects.validate(request.POST)

		# if no errors
		if not errors:
			# Get currently logged in user
			user = current_user(request)

			# Create the book
			book = Book.objects.create_book(request.POST)

			# Create the review
			if len(request.POST['content']) > 1:
				review = Review.objects.create_review(request.POST, book, user)

			# redirect to book show page
			return redirect(reverse('show_book', kwargs={'id': book.id}))

		# flash the errors
		flash_errors(request, errors)

	return redirect(reverse('add_book'))

def show(request, id):
	context = {
		'book': Book.objects.get(id=id),
	}

	return render(request, 'book_app/show.html', context)
