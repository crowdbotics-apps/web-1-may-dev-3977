# Generated by Django 2.2.12 on 2020-05-01 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_load_initial_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customtext',
            name='title',
        ),
        migrations.AddField(
            model_name='customtext',
            name='gfg',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customtext_gfg', to='home.CustomText'),
        ),
        migrations.AddField(
            model_name='customtext',
            name='hghg',
            field=models.ManyToManyField(blank=True, related_name='customtext_hghg', to='home.CustomText'),
        ),
    ]