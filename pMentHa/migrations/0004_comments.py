# Generated by Django 3.2.3 on 2021-06-02 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pMentHa', '0003_contact_birth'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clareza', models.IntegerField()),
                ('pertinencia', models.IntegerField()),
                ('help', models.IntegerField()),
                ('original', models.IntegerField()),
            ],
        ),
    ]