# Generated by Django 2.2.4 on 2019-08-18 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('descricao', models.TextField(blank=True, verbose_name='Descrição')),
                ('data_final', models.DateField(verbose_name='Data Final')),
                ('prioridade', models.CharField(choices=[('B', 'Baixa'), ('M', 'Media'), ('A', 'Alta')], max_length=1, verbose_name='prioridade')),
            ],
        ),
    ]