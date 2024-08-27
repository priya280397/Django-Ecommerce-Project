# Generated by Django 5.0.1 on 2024-02-09 17:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0016_remove_customerprofile_facebookp_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=255, null=True)),
                ('phone', models.BigIntegerField(null=True)),
                ('street', models.CharField(max_length=255, null=True)),
                ('landmark', models.CharField(max_length=255, null=True)),
                ('city', models.CharField(max_length=255, null=True)),
                ('state', models.CharField(max_length=255, null=True)),
                ('pincode', models.IntegerField(null=True)),
                ('country', models.CharField(max_length=255, null=True)),
                ('alt_phone', models.BigIntegerField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
