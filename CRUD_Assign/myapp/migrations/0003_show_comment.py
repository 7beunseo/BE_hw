# Generated by Django 4.2.1 on 2023-05-23 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_show_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='comment',
            field=models.CharField(max_length=50, null=True),
        ),
    ]