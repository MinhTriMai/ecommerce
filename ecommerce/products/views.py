from django.shortcuts import render

from .models import Product
# Create your views here.
def home(request):

	context ={'username_is':'Pham Anh Dung'}
	template = 'products/home.html'
	
	return render(request, template, context)


def all(request):
	products = Product.objects.all()
	context = {'products': products}
	template = 'products/all.html'
	return render(request,template,context)