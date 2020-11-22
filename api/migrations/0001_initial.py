# Generated by Django 3.1.3 on 2020-11-20 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('expira', models.DateField()),
                ('alerta1y', models.BooleanField(default=True)),
                ('alerta6m', models.BooleanField(default=True)),
                ('alerta3m', models.BooleanField(default=True)),
                ('alerta1m', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Documentos',
            },
        ),
    ]
