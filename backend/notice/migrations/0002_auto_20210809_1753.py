# Generated by Django 3.2.3 on 2021-08-09 08:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notice', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='student',
        ),
        migrations.AddField(
            model_name='notification',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.user'),
            preserve_default=False,
        ),
    ]
