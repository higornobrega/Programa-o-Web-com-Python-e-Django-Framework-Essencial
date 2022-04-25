from django.views.generic import TemplateView
from .models import Funcionario, Servico
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs) #Pega tudo que vier do contexto da página
        context['servicos'] = Servico.objects.order_by('?').all() #Adicionar ao contexto
        context['funcionarios'] = Funcionario.objects.order_by('?').all() #Adiciona ao contexto
        return context

