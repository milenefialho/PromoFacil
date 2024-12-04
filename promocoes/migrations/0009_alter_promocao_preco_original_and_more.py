# Generated by Django 5.0.4 on 2024-12-04 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promocoes', '0008_alter_promocao_data_inicio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocao',
            name='preco_original',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='promocao',
            name='preco_promocional',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]