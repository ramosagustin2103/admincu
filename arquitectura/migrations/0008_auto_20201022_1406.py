# Generated by Django 2.0.3 on 2020-10-22 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arquitectura', '0007_auto_20181130_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasto',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]