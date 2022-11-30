# Generated by Django 4.1.1 on 2022-11-05 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, null=True)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('update', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_no',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='staff',
            name='phone_no',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=15),
        ),
    ]