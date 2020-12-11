# Generated by Django 2.2.12 on 2020-12-11 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0008_account_androidid'),
    ]

    operations = [
        migrations.CreateModel(
            name='RandomNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=6)),
                ('issuedIn', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='account',
            name='androidID',
        ),
    ]