# Generated by Django 2.0.1 on 2018-01-09 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memehub', '0006_auto_20180109_1418'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meme',
            options={'ordering': ['title']},
        ),
        migrations.RemoveField(
            model_name='profile',
            name='seenMemes',
        ),
        migrations.AddField(
            model_name='profile',
            name='seenMemes',
            field=models.ManyToManyField(to='memehub.Meme'),
        ),
    ]
