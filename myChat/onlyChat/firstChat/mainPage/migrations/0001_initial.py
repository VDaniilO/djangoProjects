# Generated by Django 4.0.3 on 2022-05-04 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Region_name', models.CharField(db_index=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='logInf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=150)),
                ('firstName', models.CharField(max_length=150)),
                ('lastName', models.CharField(max_length=150)),
                ('photo', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_up', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='mainPage.regions')),
            ],
        ),
    ]
