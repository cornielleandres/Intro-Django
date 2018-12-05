# Generated by Django 2.1.4 on 2018-12-05 20:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ingredient_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('recipe_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='ingredient',
            name='recipe_id',
            field=models.ManyToManyField(to='recipes.Recipe'),
        ),
    ]