# Generated by Django 4.1.2 on 2022-10-15 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0002_rename_persona_familiar"),
    ]

    operations = [
        migrations.RenameModel(old_name="Familiar", new_name="Persona",),
    ]
