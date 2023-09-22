from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def home(request):
	if request.method=='POST':
		name=request.POST['name']
		email=request.POST['email']
		message=request.POST['comment']
		messages.success(request, (f'Hi {name}, your message was received, kindly await reply.'))
		return render(request, 'index2.html', {'name':name})
	return render(request, 'index2.html', {})