from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models
from stdimage.models import StdImageField

#Nomes diferentes para mídias
import uuid #Gera Strings aleatórias
def get_file_path(_intance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename
#SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify

#Classe Abstrata não é escrita no BD
class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Servico(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )    
    servico = models.CharField("Serviço", max_length=100)
    descricao = models.TextField("Descrição")
    icone = models.CharField("Icone", max_length=12, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return str(self.servico) 

class Cargo(Base):
    cargo = models.CharField("Cargo", max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return str(self.cargo)

class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio')
    image = StdImageField('Image', upload_to=get_file_path, variations={'thumb' : {'width':480, 'height':480}})
    facebook = models.CharField("Facebook", max_length=100, default='#')
    twitter = models.CharField("twitter", max_length=100, default='#')
    instagram = models.CharField("instagram", max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return str(self.nome)


class Feature(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    ) 
    titulo = models.CharField("Título", max_length=100)
    icone = models.CharField('Icone', max_length=50, choices=ICONE_CHOICES)
    descricao = models.TextField("Deacrição")

    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'

    def __str__(self):
        return str(self.titulo)