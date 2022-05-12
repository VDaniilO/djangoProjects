# Generated by Django 4.0.3 on 2022-05-11 12:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MessageChecker', '0002_alter_messages_condition_alter_messages_verify'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='user_permission',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
