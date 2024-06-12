from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    #date_of_birth = models.DateField(null=True, blank=True)
    telefone = models.TextField(max_length=11, blank=True)
    cpf = models.CharField('CPF', max_length=30, default='')
    cep = models.CharField('CEP', max_length=8, default='')
    endereço = models.CharField(max_length=40, blank=True)
    numero = models.CharField(max_length=5)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username

class ProductModel(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='produtos/')

    def __str__(self):
        return self.name
    
class VendaModel(models.Model):
    dataVenda = models.CharField(max_length=8)
    codigoVenda = models.CharField(max_length=5)
    codigoCliente = models.CharField(max_length=5)
    codigoFornecedor = models.CharField(max_length=5)
    name = models.CharField(max_length=150)
    description = models.TextField()
    quantidade = models.DecimalField(decimal_places=2, max_digits=10)
    valorUnitario = models.DecimalField(decimal_places=2, max_digits=10)
    valorTotal = models.DecimalField(decimal_places=2, max_digits=10)