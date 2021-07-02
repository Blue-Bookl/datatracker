# Generated by Django 2.2.20 on 2021-05-19 09:55

from django.db import migrations


def forward(apps, schema_editor):
    """Set is_group_conflict for ConstraintNames that need it to be True"""
    ConstraintName = apps.get_model('name', 'ConstraintName')
    ConstraintName.objects.filter(
        slug__in=['conflict', 'conflic2', 'conflic3']
    ).update(is_group_conflict=True)


def reverse(apps, schema_editor):
    pass  # nothing to be done


class Migration(migrations.Migration):
    dependencies = [
        ('name', '0024_constraintname_is_group_conflict'),
    ]

    operations = [
        migrations.RunPython(forward, reverse),
    ]