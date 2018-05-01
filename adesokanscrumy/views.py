from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime
from django.db.models.functions import Trunc
from  .models  import ScrumyUser 
from adesokanscrumy.models import ScrumyGoals, GoalStatus
from .models import ScrumyGoalsQueryset, ScrumyGoalsManager, GoalStatusManager, GoalStatusQueryset

def index(request):
    queryset= ScrumyGoals.objects.all()

    context= {
        "object_list":queryset,
        "title": "list",
    }
    return render(request,'adesokanscrumy/templates/home.html', context)
   

def home(request):
    instance= GoalStatus.objects.get(id=1)
    

    context= {
        "title" :instance.date_completed,
        "instance": instance,
    }
    return render(request,'adesokanscrumy/templates/one.html', context)
   

def move_goal(request, task_id):
    goalinstance= GoalStatus.objects.get(id=1)
    

    context= {
        "newtitle" :goalinstance.date_completed,
        "goalinstance": goalinstance,
    }
    return render(request,'adesokanscrumy/templates/movegoal.html', context)


def add_user(request ):
        newuser =ScrumyUser()
        newuser.username= "babadaradara"
        newuser.gender="female"
        newuser.roles='QA'
        newuser.email="babao@gmail.com"
        newuser.date_registered= Trunc(datetime,"day")
        newuser.save()
        
    
        output ="this is the  ', '.join([eachuser.username for eachuser in ScrumyUser.objects.all()])"
        return HttpResponse(request,output)