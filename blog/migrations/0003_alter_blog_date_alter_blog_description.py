# Generated by Django 4.1 on 2023-04-12 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_date_alter_blog_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
