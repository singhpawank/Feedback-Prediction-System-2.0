# Generated by Django 3.2.5 on 2022-03-30 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_result_score'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='visiterName',
            new_name='visitorName',
        ),
    ]