# Generated by Django 3.2.9 on 2023-02-07 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankPortal', '0007_auto_20230207_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank_portal_new',
            name='count_view',
            field=models.IntegerField(default=0, max_length=200, null=True),
        ),
    ]