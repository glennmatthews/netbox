# Generated by Django 2.2 on 2019-08-12 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0023_fix_tag_sequences'),
    ]

    operations = [
        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
            ],
            options={
                'managed': False,
            },
        ),
    ]
