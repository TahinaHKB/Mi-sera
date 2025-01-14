# Generated by Django 5.0.4 on 2024-04-07 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradePlatform', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='email',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='password',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='birth',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='member',
            name='picture',
            field=models.FileField(default='pictures/user.png', upload_to='pictures'),
        ),
    ]
