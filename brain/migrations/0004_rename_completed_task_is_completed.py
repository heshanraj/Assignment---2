# Generated by Django 4.2.13 on 2024-06-15 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brain', '0003_task_completed_alter_task_priority'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='completed',
            new_name='is_completed',
        ),
    ]
