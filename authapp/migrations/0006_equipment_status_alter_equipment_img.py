# Generated by Django 5.0.4 on 2024-05-06 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_equipment'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='status',
            field=models.CharField(default='some_default_value', max_length=100),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='img',
            field=models.ImageField(upload_to='equipment'),
        ),
    ]