# Generated by Django 2.1.15 on 2021-11-18 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimos', '0011_emprestimos_observation2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprestimos',
            name='observation2',
        ),
    ]