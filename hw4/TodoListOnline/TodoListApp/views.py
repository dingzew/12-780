# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Task
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def loadTask(request):
    tasks = Task.objects.all()
    result = ""
    for task in tasks:
        result = result + task.TaskID + ","
        result = result + task.Description + ","
        result = result + str(task.DueDate) + ","
        result = result + str(task.Status) + ";"

    result = result[:-1]

    return HttpResponse(result)


def addTaskRecord(request):
    try:
        TaskID = request.GET["TaskID"]
        Description = request.GET["Description"]
        DueDate = request.GET["DueDate"]
        Status = request.GET["Status"]

        if(Status == "on"):
            Status = bool(True)
        else:
            Status = bool(False)

        print Status
        print DueDate
        newTask = Task(TaskID=TaskID,
                         Description=Description,
                         DueDate=datetime.strptime(DueDate, '%Y-%m-%d'),
                         Status = Status
                         )
        newTask.save()
        return HttpResponse("OK")

    except:
        return HttpResponse("Failed")


def checkExistID(request):
    tasks = Task.objects.all()

    for task in tasks:
        if (task.TaskID == request.GET["TaskID"]):
            return HttpResponse("true")

    return HttpResponse("false")