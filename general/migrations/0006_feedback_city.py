# Generated by Django 2.2 on 2020-01-03 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0005_auto_20191225_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='city',
            field=models.CharField(default='test', max_length=100),
            preserve_default=False,
        ),
    ]
