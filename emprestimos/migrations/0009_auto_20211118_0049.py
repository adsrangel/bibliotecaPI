# Generated by Django 2.1.15 on 2021-11-18 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimos', '0008_auto_20211117_2355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprestimos',
            name='user',
        ),
        migrations.AlterField(
            model_name='emprestimos',
            name='data_devolucao',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emprestimos',
            name='data_emprestimo',
            field=models.DateField(blank=True, null=True),
        ),
    ]