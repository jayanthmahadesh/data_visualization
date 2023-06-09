# Generated by Django 4.1.3 on 2023-05-25 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='static/images/')),
                ('productkey', models.IntegerField()),
                ('end_year', models.IntegerField()),
                ('intensity', models.IntegerField()),
                ('sector', models.CharField(max_length=100)),
                ('topic', models.CharField(max_length=100)),
                ('insight', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=200)),
                ('region', models.CharField(max_length=100)),
                ('start_year', models.IntegerField()),
                ('impact', models.IntegerField()),
                ('added', models.CharField(max_length=100)),
                ('published', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('relevance', models.IntegerField()),
                ('pestle', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('likelihood', models.IntegerField()),
            ],
        ),
    ]
