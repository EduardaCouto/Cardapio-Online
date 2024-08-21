# Generated by Django 4.2.8 on 2024-08-17 17:22

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restricao', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('nome', models.CharField(max_length=255)),
                ('categoria', models.CharField(choices=[('CAE', 'CAE'), ('Nutricionista', 'Nutricionista'), ('Pessoa', 'Pessoa')], default='Pessoa', max_length=50)),
                ('restricao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='restricao.restricao')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
