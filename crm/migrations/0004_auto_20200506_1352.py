# Generated by Django 2.2.12 on 2020-05-06 13:52

from django.db import migrations


def render_all_markdown(apps, schema_editor):
    try:
        from wagtailmarkdown.utils import render_markdown
        from wagtailmarkdown.fields import MarkdownField
    except ImportError:
        return

    for model in apps.get_models():
        markdown_fields = [field.name for field in model._meta.fields if isinstance(field, MarkdownField)]
        if markdown_fields:
            print(f"{model.__name__}: {markdown_fields}")
        for instance in model.objects.all():
            for field in markdown_fields:
                setattr(
                    instance, field,
                    render_markdown(getattr(instance, field))
                )
            instance.save()


class Migration(migrations.Migration):
    dependencies = [
        ('crm', '0003_auto_20200504_1533'),
    ]

    operations = [
        migrations.RunPython(render_all_markdown),
    ]