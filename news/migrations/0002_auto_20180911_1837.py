# Generated by Django 2.1.1 on 2018-09-11 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporter',
            name='contact',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='reporter',
            name='email',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
