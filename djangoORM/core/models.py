from django.db import models
from django.contrib.auth import get_user_model

class Chassi(models.Model):
    numero = models.CharField('Chassi', max_length=16, help_text='Informe 16 caracteres')

    class Meta:
        verbose_name = 'Chassi'
        verbose_name_plural = 'Chassis'
    def __str__(self):
        return str(self.numero)

class Montadora(models.Model):
    nome = models.CharField("Nome", max_length=50)

    class Meta:
        verbose_name = 'Montadora'
        verbose_name_plural = 'Montadoras'

    def __str__(self):
        return str(self.nome)

#Tentar pegar uma Montadora com nome Padrão, caso não exista, crie
def set_default_montadora():
    return Montadora.objects.get_or_create(nome='Padrão')[0] # Retorna 2 parâmetros object ([0]) e boolean ([1]) 


class Carro(models.Model):
    """
    # OneToOneField
    Cada carro só pode se relacionar com um chassi
    e cada chassi só pode se relacionar com um carro
    
    # ForeignKey (One to Many)
    Cada carro tem uma montadora mas uma montadora 
    pode 'montar' vários carros.

    # ManyToMany
    Um Carro pode ser dirigido por vários motoristas
    e um motorista pode dirigir diversos carros.

    """
    chassi = models.OneToOneField(Chassi, on_delete=models.CASCADE)
    modelo = models.CharField('Modelo', max_length=30)
    motoristas = models.ManyToManyField(get_user_model())
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    montadora = models.ForeignKey(Montadora, on_delete=models.SET(set_default_montadora))
    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

    def __str__(self):
        return f'{self.montadora} {self.modelo}' 

