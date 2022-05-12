# Generated by Django 4.0.3 on 2022-05-11 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MessageChecker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='condition',
            field=models.ForeignKey(default='1', null=True, on_delete=django.db.models.deletion.PROTECT, to='MessageChecker.conditions'),
        ),
        migrations.AlterField(
            model_name='messages',
            name='verify',
            field=models.BooleanField(default=False),
        ),
    ]
