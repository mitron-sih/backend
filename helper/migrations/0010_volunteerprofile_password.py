# Generated by Django 4.0.3 on 2022-08-25 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0009_remove_profileuser_address_line_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteerprofile',
            name='password',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
