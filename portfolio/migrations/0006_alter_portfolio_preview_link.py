# Generated by Django 4.1.1 on 2023-01-06 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_portfolio_project_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='preview_link',
            field=models.URLField(),
        ),
    ]