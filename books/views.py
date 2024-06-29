from django.shortcuts import render

# Create your views here.

#for template it follows the directory as below 
#appName/template/appName/index.html 

def index(response):
    context = {'allbooks':['spiritual power', 'long term patience', 'true faith ']}
    return render(response, 'books/index.html',context)


def about(response):
    return render(response, 'books/about.html')

def base(respone):
    return render(respone, 'books/_base.html')


