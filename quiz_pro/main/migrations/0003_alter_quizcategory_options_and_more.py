# Generated by Django 4.2.2 on 2023-06-26 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_quizquestion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quizcategory',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='quizquestion',
            options={'verbose_name_plural': 'Questions'},
        ),
    ]
