# Generated by Django 5.0.7 on 2024-07-31 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_about_contact_product_alter_course_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='Title',
            field=models.CharField(default='Default Title', max_length=100, verbose_name='Title'),
            preserve_default=False,
        ),
    ]
