# Generated by Django 5.1.6 on 2025-03-16 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_culturebatch_no_of_bottles'),
    ]

    operations = [
        migrations.RenameField(
            model_name='culturebatch',
            old_name='No_of_Bottles',
            new_name='No_of_bottles',
        ),
    ]
