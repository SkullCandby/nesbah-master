# Generated by Django 3.2.9 on 2022-11-28 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20221128_1528'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='name',
            new_name='mobile',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='date_created',
        ),
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
