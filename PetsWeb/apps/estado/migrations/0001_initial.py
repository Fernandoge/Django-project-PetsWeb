# Generated by Django 2.1.3 on 2019-01-05 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('EST_COD', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('EST_NOM', models.CharField(max_length=20)),
            ],
        ),
    ]