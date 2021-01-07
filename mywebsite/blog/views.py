from django.shortcuts import render

# Create your views here.
def index(req):
    context = {

    }

    return render(req, 'index.html', context=context)

def post(req):
    context = {

    }

    return render(req, 'post.html', context=context)