from django.shortcuts import render
from .models import Aluno
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def listar_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos/listar_alunos.html', {'alunos': alunos})

@csrf_exempt
def criar_aluno(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nome = data.get('nome')
            sobrenome = data.get('sobrenome')
            cpf = data.get('cpf')
            email = data.get('email')

            if Aluno.objects.filter(cpf=cpf).exists():
                return JsonResponse({'erro': 'Existe um aluno com o mesmo cpf'})

            aluno = Aluno.objects.create(nome=nome, sobrenome=sobrenome, cpf=cpf, email=email)

            return JsonResponse({'mensagem': 'Aluno criado com sucesso'})
        except json.JSONDecodeError:
            return JsonResponse({'erro': 'JSON inválido'}, status=400)
    else:
        return JsonResponse({'erro': 'Método não suportado'}, status=400)
