# Generated by Django 2.0.3 on 2018-12-06 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0004_auto_20181130_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cierre',
            name='logo_auditor',
            field=models.ImageField(blank=True, null=True, upload_to='reportes/logos/'),
        ),
    ]