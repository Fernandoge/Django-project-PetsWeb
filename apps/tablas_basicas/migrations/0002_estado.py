# Generated by Django 2.1.5 on 2019-01-14 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablas_basicas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
    ]
