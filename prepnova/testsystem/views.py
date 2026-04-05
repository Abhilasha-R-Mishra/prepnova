from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Test, Question, Result
from django.contrib.auth.decorators import login_required
import json

from django.http import JsonResponse
import random


def home(request):
    return render(request, 'home.html')


# Predefined questions (AI simulation)
QUESTIONS = [
    "What is Python?",
    "Explain Django architecture.",
    "What is REST API?",
    "Difference between list and tuple?",
    "What is SQL JOIN?"
]

def ai_interview(request):
    return render(request, 'ai_interview.html')


def ai_response(request):
    user_input = request.GET.get('message')

    # simple logic (AI simulation)
    next_question = random.choice(QUESTIONS)

    return JsonResponse({
        "reply": f"Good answer 👍 Now next question: {next_question}"
    })


@login_required
def dashboard(request):
    tests = Test.objects.all()
    results = Result.objects.filter(user=request.user)

    labels = []
    scores = []

    for i, r in enumerate(results):
        labels.append(f"Test {i+1}")
        scores.append(r.score)

    return render(request, 'dashboard.html', {
        'tests': tests,
        'labels': json.dumps(labels),
        'scores': json.dumps(scores),
    })

# @login_required
# def dashboard(request):
#     tests = Test.objects.all()
#     return render(request, 'dashboard.html', {'tests': tests})

# @login_required
# def dashboard(request):
#     tests = Test.objects.all()
#     results = Result.objects.filter(user=request.user)

#     total_tests = results.count()
#     avg_score = 0

#     if total_tests > 0:
#         avg_score = sum([r.score for r in results]) / total_tests

#     return render(request, 'dashboard.html', {
#         'tests': tests,
#         'total_tests': total_tests,
#         'avg_score': avg_score,
#         'results': results
#     })


@login_required
def create_test(request):
    if request.method == 'POST':
        title = request.POST['title']
        category = request.POST['category']
        difficulty = request.POST['difficulty']

        test = Test.objects.create(
            title=title,
            category=category,
            difficulty=difficulty,
            created_by=request.user
        )

        return redirect('dashboard')

    return render(request, 'create_test.html')

@login_required
def attempt_test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    questions = Question.objects.filter(test=test)

    if request.method == 'POST':
        score = 0
        for q in questions:
            user_answer = request.POST.get(str(q.id))
            if user_answer == q.correct_answer:
                score += 1

        Result.objects.create(
            user=request.user,
            test=test,
            score=score,
            total=questions.count()
        )

        return redirect('result', test_id=test.id)

    return render(request, 'attempt_test.html', {'test': test, 'questions': questions})

@login_required
def result_view(request, test_id):
    result = Result.objects.filter(user=request.user, test_id=test_id).last()
    return render(request, 'result.html', {'result': result})
