# Generated by Django 2.2.19 on 2021-06-29 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('creditos', '0007_auto_20190102_1146'),
        ('expensas_pagas', '0002_clienteexp'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentoExp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.CharField(max_length=90)),
                ('cpe', models.CharField(max_length=6516)),
                ('inf_deuda', models.BooleanField(default=False)),
                ('pdf', models.FileField(blank=True, null=True, upload_to='expensas_pagas/pdf/')),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exp', to='creditos.Factura')),
            ],
        ),
    ]
