# Generated by Django 4.2 on 2023-05-04 16:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0005_studentremove"),
    ]

    operations = [
        migrations.DeleteModel(
            name="StudentRemove",
        ),
    ]
