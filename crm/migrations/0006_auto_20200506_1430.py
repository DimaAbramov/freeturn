# Generated by Django 2.2.12 on 2020-05-06 14:30

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_auto_20200506_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cvgenerationsettings',
            name='default_rate_overview',
            field=wagtail.core.fields.RichTextField(default='100 schmeckles'),
        ),
    ]