# Generated by Django 2.2.5 on 2019-09-18 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0013_auto_20190917_1030'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-shared_comment']},
        ),
    ]
