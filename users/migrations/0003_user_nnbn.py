# Generated by Django 2.2.12 on 2020-05-01 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_auto_20200501_0846"),
        ("users", "0002_auto_20200501_0816"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="nnbn",
            field=models.ManyToManyField(
                blank=True, related_name="user_nnbn", to="home.HomePage"
            ),
        ),
    ]
