# Generated by Django 5.0.3 on 2024-04-23 16:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titre', models.CharField(max_length=50)),
                ('contenu', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(upload_to='photos/%y/%m/%d')),
                ('montant', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
    ]
