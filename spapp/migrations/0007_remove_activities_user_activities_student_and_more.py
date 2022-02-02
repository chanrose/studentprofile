# Generated by Django 4.0.2 on 2022-02-02 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spapp', '0006_remove_academicrecognition_activity_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activities',
            name='user',
        ),
        migrations.AddField(
            model_name='activities',
            name='student',
            field=models.OneToOneField(default=111, on_delete=django.db.models.deletion.CASCADE, to='spapp.student'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activities',
            name='description',
            field=models.TextField(),
        ),
        migrations.CreateModel(
            name='Research',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('co_author', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=50)),
                ('published_date', models.DateField()),
                ('activity', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='research', to='spapp.activities')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resonsibility', models.TextField()),
                ('location', models.CharField(max_length=50)),
                ('activity', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='spapp.activities')),
            ],
        ),
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='internship', to='spapp.activities')),
            ],
        ),
    ]
