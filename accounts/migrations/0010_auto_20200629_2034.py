# Generated by Django 2.2.9 on 2020-06-29 19:34

import accounts.models
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200629_2030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Base_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Base_Location', models.CharField(blank=True, max_length=1000, null=True)),
                ('Storage_Space', models.CharField(blank=True, max_length=1000, null=True)),
                ('Security_Arrangements', models.CharField(blank=True, max_length=1000, null=True)),
                ('Closest_Airport', models.CharField(blank=True, max_length=1000, null=True)),
                ('Local_taxi_firms', models.CharField(blank=True, max_length=1000, null=True)),
                ('Accommodation', models.CharField(blank=True, max_length=1000, null=True)),
                ('Base_facilities', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='base_details',
            field=djongo.models.fields.EmbeddedModelField(model_container=accounts.models.Base_Details, model_form_class=accounts.models.Base_DetailsForm, null=True),
        ),
    ]
