# Generated by Django 2.0.3 on 2018-11-02 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arquitectura', '0002_auto_20181030_1145'),
        ('creditos', '0002_factura_observacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='credito',
            name='accesorios',
        ),
        migrations.AddField(
            model_name='credito',
            name='acc_bonif',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='acc_bonif', to='arquitectura.Accesorio'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='facturas/pdf/'),
        ),
    ]