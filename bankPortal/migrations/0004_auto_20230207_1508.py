# Generated by Django 3.2.9 on 2023-02-07 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankPortal', '0003_auto_20230202_0353'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank_portal_new',
            name='view_count',
            field=models.IntegerField(default=0, max_length=999),
        ),
        migrations.AlterField(
            model_name='bank_portal_new',
            name='count',
            field=models.IntegerField(default=0, max_length=200, null=True),
        ),
    ]