# Generated by Django 2.0.9 on 2019-01-15 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0038_auto_20181227_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectpage',
            name='technologies_temp',
            field=models.ManyToManyField(related_name='projects', to='home.TechnologyInfo'),
        ),
    ]
