# Generated by Django 4.2.10 on 2024-03-03 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_alter_task_options_rename_due_date_task_due_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='reviewed',
            field=models.BooleanField(default=False),
        ),
    ]
