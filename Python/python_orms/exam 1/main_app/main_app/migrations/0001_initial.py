# Generated by Django 4.2.4 on 2023-11-23 16:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=120, validators=[django.core.validators.MinLengthValidator(2)])),
                ('birth_date', models.DateField(default='1900-01-01')),
                ('nationality', models.CharField(default='Unknown', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main_app.basemodel')),
                ('is_awarded', models.BooleanField(default=False)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
            bases=('main_app.basemodel',),
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main_app.basemodel')),
                ('years_of_experience', models.SmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
            ],
            bases=('main_app.basemodel',),
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, validators=[django.core.validators.MinLengthValidator(5)])),
                ('release_date', models.DateField()),
                ('storyline', models.TextField(blank=True, null=True)),
                ('genre', models.CharField(choices=[('Action', 'Action'), ('Comedy', 'Comedy'), ('Drama', 'Drama'), ('Other', 'Other')], default='Other', max_length=6)),
                ('rating', models.DecimalField(decimal_places=1, default=0.0, max_digits=3, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)])),
                ('is_classic', models.BooleanField(default=False)),
                ('is_awarded', models.BooleanField(default=False)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('actors', models.ManyToManyField(related_name='actor_movie', to='main_app.actor')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='director_movie', to='main_app.director')),
                ('starring_actor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='starring_actor_movie', to='main_app.actor')),
            ],
        ),
    ]