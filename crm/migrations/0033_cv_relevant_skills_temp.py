# Generated by Django 2.0.9 on 2019-01-15 16:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('home', '0044_auto_20190115_1559'),
        ('crm', '0032_auto_20181209_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='relevant_skills_temp',
            field=models.ManyToManyField(
                blank=True,
                help_text='Technologies to be included, will be automatically formed to look relevant',
                to='home.TechnologyInfo'),
        ),
    ]