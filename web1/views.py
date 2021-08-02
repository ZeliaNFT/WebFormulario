from django.shortcuts import render
from .forms import ContatoForm
from django.contrib import messages
from web1.models import Produto


# Create your views here.
def index(request):
    produtos = Produto.objects.all()

    testeChave = {
        'produtos': produtos
    }
    return render(request, 'index.html',testeChave)


def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':

        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            form.send_mail()

            messages.success(request, 'E-mail enviado com sucesso')
            """
            print('Mensagem Enviada')
            print(f'Nome: {nome}')
            print(f'E-mail: {email}')
            print(f'Assunto: {assunto}')
            print(f'Mensagem: {mensagem}')
            """
            form = ContatoForm()

        else:
            messages.error(request, 'Erro ao enviar e-mail')
    context = {

        'form': form

    }
    return render(request, 'contato.html', context)

def produto(request, id):
    produto = Produto.objects.get(id=id)
    context = {
        'produto': produto

    }
    return render(request, 'produto.html',context)