# Generated by Django 4.0 on 2021-12-26 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_user_first_name_alter_user_username'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postreadhistory',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='authentication.user'),
            preserve_default=False,
        ),
    ]
