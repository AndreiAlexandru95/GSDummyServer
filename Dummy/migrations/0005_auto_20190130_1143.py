# Generated by Django 2.1.5 on 2019-01-30 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dummy', '0004_obz_symbol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symbol',
            name='author',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='symbol',
            name='author_url',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='symbol',
            name='extension',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='symbol',
            name='image_url',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='symbol',
            name='license',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='symbol',
            name='locale',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='symbol',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='symbol',
            name='source_url',
            field=models.TextField(blank=True, null=True),
        ),
    ]