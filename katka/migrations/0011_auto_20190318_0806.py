# Generated by Django 2.1.7 on 2019-03-18 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('katka', '0010_rename_scmtype'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='credential',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='credential',
            name='slug',
        ),
    ]
