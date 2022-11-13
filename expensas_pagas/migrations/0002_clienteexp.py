# Generated by Django 2.2.19 on 2021-06-29 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consorcios', '0002_consorcio_costo_mp'),
        ('expensas_pagas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClienteExp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_exp', models.PositiveIntegerField(blank=True, null=True)),
                ('di_exp', models.PositiveIntegerField(blank=True, null=True)),
                ('consorcio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exp', to='consorcios.Consorcio')),
            ],
        ),
    ]
