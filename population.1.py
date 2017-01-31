import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 
'vpstable.settings')

import django
django.setup()
from django.utils import timezone
from polls.models import Question, Choice

def populate():
    python_choice = [
        {'choice_text' : 'pchoice1', 
        'pub_date' : 'timezone.now()'}, 
        {'choice_text' : 'pchoice2', 
        'pub_date' : 'timezone.now()'}, 
        {'choice_text' : 'pchoice3', 
        'pub_date' : 'timezone.now()'}, 
        {'choice_text' : 'pchoice4', 
        'pub_date' : 'timezone.now()'}
        ]

    django_choice = [
        {'choice_text' : 'jchoice1', 
        'pub_date' : 'timezone.now()'}, 
        {'choice_text' : 'jchoice2', 
        'pub_date' : 'timezone.now()'}, 
        {'choice_text' : 'jchoice3', 
        'pub_date' : 'timezone.now()'}, 
        {'choice_text' : 'jchoice4', 
        'pub_date' : 'timezone.now()'}
        ]

    other_choice = [
        {'choice_text' : 'ochoice1', 
        'pub_date' : 'timezone.now()'}, 
        {'choice_text' : 'ochoice2', 
        'pub_date' : 'timezone.now()'}, 
        {'choice_text' : 'ochoice3', 
        'pub_date' : 'timezone.now()'}, 
        {'choice_text' : 'ochoice4', 
        'pub_date' : 'timezone.now()'}
        ]


    qts = {
        "python": {"choice": python_choice},
        "django": {"choice": django_choice},
        "other": {"choice": other_choice}
          }


    for qt, qt_data in qts.items():
        q = add_question(qt)
        for c in qt_data["choice"]:
            add_choice(q, c["choice"], c["pub_date"])

    for q in Question.objects.all():
        for c in Choice.objects.filter(question=q):
            print("- {0} - {1}".format(str(q), str(c)))




def add_choice(qt, choice_text, vote=0):
    c = Choice.objects.get_or_create(question=qt, choice_text=choice_text)[0]
    c.vote = vote
    c.save()
    return c

def add_question(question_text):
    q = Question.objects.get_or_create(question_text=question_text)[0]
    q.save()
    return q

if __name__ == '__main__':
    print('开始生成内容...')
    populate()