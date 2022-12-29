# Generated by Django 4.1.2 on 2022-11-24 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AdminApp', '0002_userinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('grocery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.userinfo')),
            ],
            options={
                'db_table': 'MyCart',
            },
        ),
    ]