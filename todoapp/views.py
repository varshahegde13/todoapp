from django.shortcuts import render
from todoapp.models import Task

# Create your views here.
def home(request):
    context = {'success': False}
    if request.method == "POST":
        # handle the post
        title = request.POST['title']
        desc = request.POST['desc']
        print(title,desc)
        ins = Task(taskTitle=title, taskDesc=desc)
        ins.save()
        context = {'success': True}




    return render(request, 'index.html', context)

def tasks(request):
    allTasks = Task.objects.all()
    # print(allTasks)
    context = {'tasks': allTasks}
    return render(request, 'tasks.html', context)