# Generated by Django 3.0.6 on 2020-05-22 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_chatter_online'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatter',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
    ]
