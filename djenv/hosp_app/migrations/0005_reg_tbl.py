# Generated by Django 5.2.3 on 2025-06-24 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosp_app', '0004_rename_hosp_tbl_dept_tbl'),
    ]

    operations = [
        migrations.CreateModel(
            name='reg_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
                ('mob', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('user_type', models.CharField(max_length=20)),
            ],
        ),
    ]
