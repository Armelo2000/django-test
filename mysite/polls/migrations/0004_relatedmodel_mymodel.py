# Generated by Django 4.0.3 on 2024-02-03 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_rename_zip_contact_zipcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelatedModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=8)),
                ('city', models.CharField(max_length=100)),
                ('field_to_update', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('one_to_one_field', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='polls.relatedmodel')),
            ],
        ),
    ]