# Generated by Django 4.2.3 on 2023-07-21 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('user_email', models.EmailField(max_length=255)),
                ('user_password', models.CharField(max_length=50)),
            ],
        ),
    ]
