# Generated by Django 3.2.4 on 2021-06-22 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=150)),
                ('full_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postal_code', models.IntegerField()),
                ('municipality', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('primary', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.user')),
            ],
        ),
    ]