from django.contrib import messages
from django.shortcuts import render
from .forms import ContatoForm, ProdutoModelForm
# Create your views here.
def index(request):
    return render(request, 'index.html')


def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']
            print('Mensagem enviar')
            print(f'Nome: {nome}')
            print(f'Email: {email}')
            print(f'Assunto: {assunto}')
            print(f'Mensagem: {mensagem}')
            messages.success(request, 'Enviado com sucesso')
            form.send_mail()
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar e-mail')
    context = {
        'form':form
    }
    return render(request,'contato.html', context)


def produto(request):
    form = ProdutoModelForm(request.POST, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # prod = form.save(commit=False)

            # print(f'Nome: {prod.nome}')
            # print(f'preco: {prod.preco}')
            # print(f'estoque: {prod.estoque}')
            # print(f'imagem: {prod.imagem}')
            messages.success(request, 'Produto Salvo com sucesso.')
            form = ProdutoModelForm()

        else:
            messages.error(request, 'Erro ao salvar produto.')

    else:
        form = ProdutoModelForm()
    context = { 
        'form' : form,
    }
    return render(request, 'produto.html', context)