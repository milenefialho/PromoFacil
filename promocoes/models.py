from django.db import models

CATEGORIAS = [
    ('ELETRONICO', 'Eletrônico'),
    ('ROUPA', 'Roupa'),
    ('ALIMENTO', 'Alimento')
]

class Promocao(models.Model):
	nome_produto = models.CharField(max_length = 100)
	data_cadastro = models.DateField()
	descricao = models.TextField()
	preco_original = models.DecimalField(max_digits=10, decimal_places=2)
	preco_promocional = models.DecimalField(max_digits=10, decimal_places=2)
	data_inicio = models.DateTimeField()
	data_termino = models.DateTimeField()
	disponibilidade = models.BooleanField(default=True)
	categoria = models.CharField(max_length=20, choices=CATEGORIAS)

	def __str__(self):
		return self.nome_produto


