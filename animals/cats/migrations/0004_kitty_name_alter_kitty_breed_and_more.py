# Generated by Django 5.1.1 on 2024-10-03 12:30

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0003_kittyrating_owner_alter_kittyrating_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitty',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='kitty',
            name='breed',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kitten', to='cats.breed'),
        ),
        migrations.AlterField(
            model_name='kittyrating',
            name='rating',
            field=models.IntegerField(default=None, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Рейтинг'),
        ),
    ]
