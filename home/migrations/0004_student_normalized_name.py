# Generated by Django 3.1.3 on 2021-01-01 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_student_social_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='normalized_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
