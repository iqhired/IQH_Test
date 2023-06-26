from django.shortcuts import render
from . import forms
from . import models



# Create your views here.

def home(request):
    return render(request, 'home.html')

def register(request):
    msg=None
    form=forms.RegisterUser
    if request.method=='POST':
        form=forms.RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            msg='Data has been added'
    return render(request, 'registration/register.html',{'form':form,msg:'msg'})

def all_categories(request):
    catData=models.QuizCategory.objects.all
    return render(request, 'all-category.html',{'data':catData})

def category_questions(request,cat_id):
  category=models.QuizCategory.objects.get(id=cat_id)
  questions=models.QuizQuestion.objects.filter(category=category )
  return render(request, 'category-questions.html',{'data':questions})
