from django.shortcuts import render
from .models import Questao
from django.http import HttpResponse

def get_quiz(request):
    questao = Questao.objects.order_by('?').first()
    context = {
        'questao': questao
    }
    return render(request, 'quiz/quiz.html', context)

def get_resposta(request):
    resposta = request.POST.get('resposta')

    if resposta == 'True':
        return HttpResponse('<p style="color:green"> Resposta Corrreta! </p>')
    elif resposta == 'False':
        return HttpResponse('<p style="color:red"> Resposta Incorrreta. </p>')
    else:
        return HttpResponse('<p style="color:grey"> Selecione uma alternativa. </p>')
