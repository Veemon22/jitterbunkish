# Generated by Django 3.2 on 2025-06-17 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotes.source'),
        ),
    ]
