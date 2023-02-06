from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.db import models
from django.forms import ModelForm
from django import forms
from django_pandas.managers import DataFrameManager



EMPRESA = (
    ('3stamina', '3stamina'),
    ('OUTRA','OUTRA'),
)


TIPO = (
    ('Despesa', 'Despesa'),
    ('Receita','Receita'),
    ('Saldo','Saldo'),
    ('Reserva','Reserva'),
    ('Transferencia','Transferencia'),

)

CATEGORIA = (
    ('Alimentação','Alimentação'),
    ('Blackbird Setup','Blackbird Setup'),
    ('Cartão de Crédito','Cartão de Crédito'),
    ('COFINS','COFINS'),
    ('Comercial','Comercial'),
    ('Comissão','Comercial'),
    ('Contabilidade','Contabilidade'),
    ('Convênio Médico','Convênio Médico'),
    ('Convênio Odontológico','Convênio Odontológico'),
    ('CSLL','CSLL'),
    ('DAS','DAS'),
    ('Despesa Administrativa','Despesa Administrativa'),
    ('Despesa Financeira','Despesa Financeira'),
    ('Emprestimos','Emprestimos'),
    ('GPS','GPS'),
    ('Imposto','Imposto'),
    ('Infraestrutura','Infraestrutura'),
    ('INSS','INSS'),
    ('Internet','Internet'),
    ('Investimento','Investimento'),
    ('IOF','IOF'),
    ('IRRF','IRRF'),
    ('ISS','ISS'),
    ('Juros','Juros'),
    ('Motoboy','Motoboy'),
    ('Movimentação','Movimentação'),
    ('Multa','Multa'),
    ('PIS','PIS'),
    ('Prejuizo','Prejuizo'),
    ('Pró Labore','Pró Labore'),
    ('Projetos','Projetos'),
    ('Recisão','Recisão'),
    ('Reserva U3','Reserva U3'),
    ('Salário','Salário'),
    ('Saldo 2016','Saldo 2016'),
    ('Seguro','Seguro'),
    ('Vale Refeição','Vale Refeição'),
    ('Vale Transporte','Vale Transporte'),
    ('Venda Ativo','Venda Ativo'),
)

STATUS = (
    ('Pago', 'Pago'),
    ('Pendente','Pendente'),
)





class Accounting(models.Model):
    geralId = models.IntegerField()
    nr = models.CharField(max_length=20,help_text='Numero Documento',blank=True)
    dataMovimento = models.DateField()
    unidade = models.CharField(max_length=20,choices=EMPRESA,help_text='Insira a unidade',blank=False)
    tipo = models.CharField(max_length=20,choices=TIPO,help_text='Insira o tipo',blank=False)
    categoria = models.CharField(max_length=20,choices=CATEGORIA,help_text='Insira a categoria',blank=True)
    origem = models.CharField(max_length=50, help_text='Insira a origem',blank=True)
    destino = models.CharField(max_length=50, help_text='Insira o destino',blank=True)
    observacao = models.CharField(max_length=200, help_text='Insira o historico',blank=True)
    valorReais = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2)
    status = models.CharField(max_length=20,choices=STATUS,help_text='Insira o status',blank=False)
    pdobjects = DataFrameManager()
    class Meta:
        unique_together = ['dataMovimento','valorReais','observacao','status']

    def __str__(self):
        return self.destino
