# Generated by Django 5.0 on 2024-02-02 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0010_alter_customerprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerprofile',
            name='profileImage',
            field=models.ImageField(null=True, upload_to='CustomerProfileImages/'),
        ),
    ]
