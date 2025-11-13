from django.shortcuts import render

# Create your views here.
def index(request):
    n={'s':[1,2,3,4,5]}
    return render(request,'index.html',n)