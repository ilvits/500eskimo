# Generated by Django 3.2.5 on 2021-07-14 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_alter_icecream_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icecream',
            name='active',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='icecream',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='icecream',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/icecream'),
        ),
    ]