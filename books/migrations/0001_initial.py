# Generated by Django 2.0.9 on 2018-11-26 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=255, verbose_name='Название книги')),
                ('authors_info', models.TextField(verbose_name='Информация об авторах')),
                ('isbn', models.CharField(max_length=20, unique=True, verbose_name='ISBN книги')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='Цена книги')),
            ],
            options={
                'verbose_name': 'Книга',
                'ordering': ['book_title'],
                'verbose_name_plural': 'Книги',
            },
        ),
    ]