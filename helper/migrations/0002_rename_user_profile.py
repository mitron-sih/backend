# Generated by Django 4.1 on 2022-08-22 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("helper", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(old_name="User", new_name="Profile",),
    ]
