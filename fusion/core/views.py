from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import ContatoForm
from .models import Funcionario, Servico, Feature

#TemplateView para templates normais sem forms
# class IndexView(TemplateView):
#     template_name = 'index.html'

#     def get_context_data(self, **kwargs):
#         context = super(IndexView, self).get_context_data(**kwargs) #Pega tudo que vier do contexto da página
#         context['servicos'] = Servico.objects.order_by('?').all() #Adicionar ao contexto
#         context['funcionarios'] = Funcionario.objects.order_by('?').all() #Adiciona ao contexto
#         context['feature'] = Feature.objects.order_by('?').all() #Adiciona ao contexto
#         return context



#FormView para templates com forms
class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs) #Pega tudo que vier do contexto da página
        context['servicos'] = Servico.objects.order_by('?').all() #Adicionar ao contexto
        context['funcionarios'] = Funcionario.objects.order_by('?').all() #Adiciona ao contexto
        context['feature'] = Feature.objects.order_by('?').all() #Adiciona ao contexto
        return context
    
    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'Email enviado com sucesso')

        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar mensagem')
        return super(IndexView, self).form_invalid(form, *args, **kwargs) 
