from django.shortcuts import render
from . models import department
# Create your views here.
def index(request):
    s={'m':department.objects.all()}
    return render(request,'index.html',s)
