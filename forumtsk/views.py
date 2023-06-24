from django.shortcuts import render
from .models import Question
from .forms import Forumform
from django.views import generic

# Create your views here.


class Forumlist(generic.ListView):   # cbv dann url , dann rename den html , dann in html object_list or post_list 
    model = Question


class Forumdetail(generic.DetailView):   # cbv dann url , dann rename den html , dann in html object or post 
    model = Question
    

class Forumcreate(generic.CreateView):  # cbv dann url , dann rename den html , dann in html
    model = Question
    fields =['question','name','date','tags']
    success_url ='/forum/'

class Forumedit(generic.UpdateView):
    model = Question
    fields =['question','name','date','tags']
    success_url ='/forum/'
    template_name = 'forum/edit.html'
    
class Forumdelete(generic.DeleteView):
    model = Question
    success_url ='/forum/'
    