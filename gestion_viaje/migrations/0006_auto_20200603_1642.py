# Generated by Django 3.0.6 on 2020-06-03 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_viaje', '0005_auto_20200527_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kilometro',
            name='tipo',
            field=models.CharField(choices=[('1', 'Didi'), ('2', 'Uber'), ('3', 'Cabify'), ('99', 'Familiar')], default='99', max_length=2),
        ),
    ]
