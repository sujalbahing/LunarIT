# Generated by Django 5.0.7 on 2024-08-10 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_contact_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancyform',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]
