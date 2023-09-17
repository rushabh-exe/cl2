# Generated by Django 4.2.4 on 2023-09-15 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='addProduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.DateTimeField(auto_now_add=True)),
                ('target', models.IntegerField(default=0, help_text='Target value in MT')),
            ],
        ),
    ]
