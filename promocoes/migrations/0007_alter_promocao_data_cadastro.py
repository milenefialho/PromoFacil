# Generated by Django 5.0.4 on 2024-12-04 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promocoes', '0006_alter_empresa_email_alter_empresa_endereco_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocao',
            name='data_cadastro',
            field=models.DateField(blank=True, null=True),
        ),
    ]