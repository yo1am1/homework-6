# Generated by Django 4.2 on 2023-05-04 16:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0007_student_delete"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="delete",
            field=models.IntegerField(default=None),
        ),
    ]