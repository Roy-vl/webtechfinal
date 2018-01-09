# Generated by Django 2.0.1 on 2018-01-09 11:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='./memes')),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('categories', models.CharField(choices=[('CU', 'Cute'), ('FU', 'Funny'), ('DA', 'Dank'), ('OS', 'Only Smart People Will Understand')], default='DA', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avater', models.ImageField(upload_to='')),
                ('fb_link', models.URLField()),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(blank=True, max_length=2, null=True)),
                ('top_3_cat', models.CharField(choices=[('CU', 'Cute'), ('FU', 'Funny'), ('DA', 'Dank'), ('OS', 'Only Smart People Will Understand')], default='DA', max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30)),
            ],
        ),
    ]