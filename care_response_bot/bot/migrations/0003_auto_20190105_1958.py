# Generated by Django 2.1.4 on 2019-01-05 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_botresponse_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='botresponse',
            name='answer',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='botresponse',
            name='name',
            field=models.CharField(default='', max_length=70),
        ),
    ]
