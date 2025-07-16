from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import problem
# Create your views here.

def main(request):
    template=loader.get_template('home.html')
    return HttpResponse(template.render())
    
def problems_list(request):
    problems=problem.objects.all().values()
    template=loader.get_template('problems_list.html')
    context={
        'problems':problems,
    }
    return HttpResponse(template.render(context,request))

def problem_details(request,id):
    p=problem.objects.get(id=id)
    template=loader.get_template('problem_details.html')
    context={
        'problem':p,
    }
    return HttpResponse(template.render(context,request))

def contest(request):
    template=loader.get_template('contest.html')
    return HttpResponse(template.render())
