from django.shortcuts import render

def Home(request):
    return render(request, 'netflix_app/index.html')
