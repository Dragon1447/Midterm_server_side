from django.shortcuts import render , redirect

# Create your views here.
from django.http import HttpResponse
from .models import Question, Choice
from django.views import View

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")
    qestion_num = latest_question_list.count()
    context = {"latested": latest_question_list,
               "num": qestion_num}
    return render(request, "index.html", context)


def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, "detail.html", {
        "question": question,
        "choices": question.choice_set.all().order_by("choice_text")
    })

def vote(request, question_id):
    question = Question.objects.get(pk=question_id)

    if request.method == "GET":
        return render(request, "vote.html", {
            "question": question,
            "choices": question.choice_set.all().order_by("choice_text")
        })
    elif request.method == "POST":
        choice_id = request.POST.get('choice')
        choice = Choice.objects.get(pk=choice_id)
        choice.votes += 1
        choice.save()
        return redirect("detail", question_id=question_id)

class IndexView(View):

    def get(self, request):
        latest_question_list = Question.objects.order_by("-pub_date")[:5]
        context = {"latest_question_list": latest_question_list}
        return render(request, "index.html", context)

class PollView(View):

    def get(self, request, question_id):
        question = Question.objects.get(pk=question_id)
        return render(request, "detail.html", {
            "question": question,
            "choices": question.choice_set.all()
        })

class VoteView(View):

    def get(self, request, question_id):
        question = Question.objects.get(pk=question_id)
        return render(request, "vote.html", {
            "question": question,
            "choices": question.choice_set.all()
        })
    
    def post(self, request, question_id):
        choice_id = request.POST.get('choice')
        choice = Choice.objects.get(pk=choice_id)
        choice.votes += 1
        choice.save()
        return redirect("detail", question_id=question_id)