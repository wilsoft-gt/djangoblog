# Generated by Django 2.2.4 on 2019-11-15 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20191112_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogposts',
            name='post_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
