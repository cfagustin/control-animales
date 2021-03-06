# Generated by Django 3.1.5 on 2021-01-24 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50, verbose_name='tipo alimento')),
            ],
        ),
        migrations.CreateModel(
            name='Alimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_alimento', models.CharField(max_length=50, verbose_name='nombre alimento')),
                ('cantidad', models.IntegerField(verbose_name='cantidad')),
                ('tipo_alimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alimentos.tipo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.usuario')),
            ],
        ),
    ]
