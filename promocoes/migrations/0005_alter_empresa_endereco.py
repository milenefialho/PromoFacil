# Generated by Django 5.0.4 on 2024-11-22 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promocoes', '0004_empresa_produto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='endereco',
            field=models.TextField(),
        ),
    ]
