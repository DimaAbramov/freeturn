# Generated by Django 2.0.9 on 2019-01-15 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0034_remove_cv_relevant_skills'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cv',
            old_name='relevant_skills_temp',
            new_name='relevant_skills',
        ),
    ]