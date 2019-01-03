# Generated by Django 2.1.2 on 2018-12-31 09:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jedzonko', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_type', models.CharField(max_length=16)),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('ingredients', models.TextField()),
                ('description', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('preparation_time', models.IntegerField(verbose_name=django.core.validators.MinValueValidator(1))),
                ('votes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RecipePlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_name', models.CharField(max_length=255)),
                ('order', models.IntegerField()),
                ('day_name_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dayname', to='jedzonko.DayName')),
            ],
        ),
        migrations.AlterField(
            model_name='plan',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AddField(
            model_name='recipeplan',
            name='plan_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan', to='jedzonko.Plan'),
        ),
        migrations.AddField(
            model_name='recipeplan',
            name='recipe_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe', to='jedzonko.Recipe'),
        ),
    ]
