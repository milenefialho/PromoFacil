# Generated by Django 5.0.4 on 2024-12-04 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('promocoes', '0014_alter_promocao_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='promocao',
            unique_together={('nome_produto', 'categoria', 'data_inicio', 'data_termino')},
        ),
    ]