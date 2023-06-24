from django.shortcuts import render
from .models import Question
from .forms import Forumform
from django.views import generic

# Create your views here.


class Forumlist(generic.ListView):   # cbv dann url , dann rename den html , dann in html object_list or post_list 
    model = Question


class Forumdetail(generic.DetailView):   # cbv dann url , dann rename den html , dann in html object or post 
    model = Question
    

class Forumcreate(generic.CreateView):
    model = Question
    fields =['question','name','date','tags']

def new_question(request):
    if request.method == 'POST':
        form = Forumform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = Forumform()
    return render(request,'forumtsk/new.html',{'form':form})