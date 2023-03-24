# Generated by Django 4.1.6 on 2023-03-23 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название расписания')),
                ('col', models.CharField(max_length=250, verbose_name='Количество классов')),
                ('col_subject', models.CharField(max_length=50, verbose_name='Колличество предметов')),
                ('subjects', models.TextField(verbose_name='Перечислите предметы')),
            ],
            options={
                'verbose_name': 'Расписание',
                'verbose_name_plural': 'Расписание',
            },
        ),
    ]