from django.db import models


sexo_choices = ('M','Masculino'),('F','Feminino')

class Formulario(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    data_nascimento = models.DateField(blank=True, null=True)
    email = models.EmailField(max_length=120)
    telefone = models.CharField(max_length=11)
    sexo = models.CharField(max_length=1, choices=sexo_choices)

    def __str__(self):
        return self.nome