# Generated by Django 3.2.8 on 2021-11-21 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spapp', '0003_alter_student_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
    ]
