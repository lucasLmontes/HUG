# Generated by Django 4.2.6 on 2023-10-16 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0005_publicacao_tipopubli_aluno_email_professor_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Responsavel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='Nome', max_length=100, verbose_name='Nome')),
                ('dataNasc', models.DateField(blank=True, help_text='Formato DD/MM/AAAA', null=True, verbose_name='Data de Nascimento')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Responsável',
                'verbose_name_plural': 'Responsáveis',
            },
        ),
        migrations.DeleteModel(
            name='TipoPubli',
        ),
        migrations.RemoveField(
            model_name='publicacao',
            name='tipo',
        ),
        migrations.AddField(
            model_name='publicacao',
            name='titulo',
            field=models.CharField(default='Título', max_length=30, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='publicacao',
            name='descricao',
            field=models.TextField(max_length=200, verbose_name='Descrição'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='responsaveis',
            field=models.ManyToManyField(blank=True, to='aplic.responsavel'),
        ),
    ]