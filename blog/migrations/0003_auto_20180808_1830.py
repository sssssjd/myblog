# Generated by Django 2.1 on 2018-08-08 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_pub_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_time',
            field=models.DateTimeField(null=True),
        ),
    ]
