# Generated by Django 3.1.4 on 2021-03-10 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='picture',
            field=models.ImageField(null=True, upload_to='student_photos/'),
        ),
    ]