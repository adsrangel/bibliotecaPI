# Generated by Django 2.1.15 on 2021-11-18 02:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimos', '0004_emprestimos_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprestimos',
            name='data_devolucao',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]