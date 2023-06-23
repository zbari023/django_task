from django.shortcuts import render
from .models import Question
from .forms import Forumform

# Create your views here.
def forum_list(request):
    data = Question.objects.all()
    return render(request,'forumtsk/index.html',{'forumtsks':data})

def forum_detail(request,forum_id):
    data = Question.objects.get(id=forum_id)
    return render(request,'forumtsk/detail.html',{'forumtsks':data})


def new_question(request):
    if request.method == 'POST':
        form = Forumform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = Forumform()
    return render(request,'forumtsk/new.html',{'form':form})