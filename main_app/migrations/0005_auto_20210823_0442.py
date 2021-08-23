# Generated by Django 3.2.4 on 2021-08-23 04:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0004_toy'),
    ]

    operations = [
        migrations.AddField(
            model_name='betta',
            name='toys',
            field=models.ManyToManyField(to='main_app.Toy'),
        ),
        migrations.AddField(
            model_name='betta',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
