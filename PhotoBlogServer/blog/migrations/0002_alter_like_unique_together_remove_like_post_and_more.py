# Generated by Django 5.1.2 on 2024-11-05 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='like',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='like',
            name='post',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
