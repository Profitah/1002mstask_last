# Generated by Django 4.0.4 on 2022-10-01 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashbookapp', '0018_alter_cashbook_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashbook',
            name='content',
            field=models.TextField(null=True),
        ),
    ]
