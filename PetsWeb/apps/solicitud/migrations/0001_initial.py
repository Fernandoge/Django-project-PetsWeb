# Generated by Django 2.1.3 on 2019-01-05 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mascota', '0001_initial'),
        ('estado', '0001_initial'),
        ('adoptante', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('SOL_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('SOL_FEC', models.DateField()),
                ('SOL_EST', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='estado.Estado')),
                ('SOL_MAS', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mascota.Mascota')),
                ('SOL_RUN', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adoptante.Adoptante')),
            ],
        ),
    ]
