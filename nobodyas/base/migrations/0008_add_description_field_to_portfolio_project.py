# Generated by Django 4.2.5 on 2023-10-14 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_add_portfolio_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioproject',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
