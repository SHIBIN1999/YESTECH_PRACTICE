from django.shortcuts import render

# Create your views here.
def index(request):
    n={'s':['orange','apple']}
    return render(request,'index.html',n)