# Generated by Django 4.0.5 on 2022-07-04 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_signup'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Signup',
            new_name='SignUpForm',
        ),
    ]