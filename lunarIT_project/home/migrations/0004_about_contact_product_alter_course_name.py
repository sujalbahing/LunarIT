# Generated by Django 5.0.7 on 2024-07-31 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_course_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200, verbose_name='Name')),
                ('Image', models.ImageField(blank=True, upload_to='images/')),
                ('Description', models.TextField(max_length=100, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, verbose_name='Name')),
                ('Email', models.EmailField(max_length=254, verbose_name='Email')),
                ('Subject', models.CharField(max_length=100, verbose_name='Subject')),
                ('Phone', models.CharField(max_length=15, verbose_name='Phone')),
                ('Message', models.TextField(verbose_name='Message')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, verbose_name='Name')),
                ('Image', models.ImageField(blank=True, upload_to='images/')),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('Description', models.TextField(max_length=100, verbose_name='Description')),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='Name',
            field=models.CharField(max_length=200, verbose_name='Name'),
        ),
    ]
