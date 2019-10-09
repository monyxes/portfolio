from django.shortcuts import render
from .models import jobs
def home(request):
    job=jobs.objects
    return render(request,'jobs/home.html',{'jobs':job})
