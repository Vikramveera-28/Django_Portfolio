from django.shortcuts import render, get_object_or_404
from .models import Jobs
# Create your views here.

def homePage(request):
    jobs = Jobs.objects.all()
    return render(request, "Index.html", {'jobs': jobs})

def detailsPage(request, job_id):
    print(job_id)
    job = get_object_or_404(Jobs, pk=job_id)
    return render(request, "Details.html", {'job': job})