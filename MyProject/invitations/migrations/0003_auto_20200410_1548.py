# Generated by Django 3.0.5 on 2020-04-10 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invitations', '0002_auto_20200410_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='inviter_user_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]