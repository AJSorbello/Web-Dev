# Generated by Django 5.1 on 2024-08-23 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author_name',
            field=models.CharField(default='Unknown Author', max_length=120),
        ),
        migrations.AddField(
            model_name='book',
            name='book_type',
            field=models.CharField(choices=[('hardcover', 'Hard cover'), ('ebook', 'E-Book'), ('audiobook', 'Audiobook')], default='hardcover', max_length=12),
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('classic', 'Classic'), ('romantic', 'Romantic'), ('comic', 'Comic'), ('fantasy', 'Fantasy'), ('horror', 'Horror'), ('educational', 'Educational')], default='classic', max_length=12),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.FloatField(default=0.0, help_text='in US dollars $'),
        ),
    ]
