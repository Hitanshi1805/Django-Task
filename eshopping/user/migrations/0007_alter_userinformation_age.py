# Generated by Django 4.0.3 on 2023-02-23 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_userinformation_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='age',
            field=models.DecimalField(decimal_places=0, default=None, max_digits=5),
        ),
    ]
