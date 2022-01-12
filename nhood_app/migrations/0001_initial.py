# Generated by Django 3.2.7 on 2022-01-12 22:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NeighbourHood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('locality', models.CharField(blank=True, max_length=200)),
                ('occupants_count', models.IntegerField(blank=True, null=True)),
                ('hood_pic', models.ImageField(default='default.png', upload_to='hoods/profiles/')),
                ('police_call', models.IntegerField(blank=True, null=True)),
                ('hospital_call', models.IntegerField(blank=True, null=True)),
                ('Fire_call', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(blank=True, max_length=255, null=True)),
                ('profile_pic', models.ImageField(default='default.png', upload_to='images/profile/')),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('hood_name', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, choices=[('insecurity', 'insecurity'), ('death', 'death'), ('advertisement', 'advertisement'), ('fundraising', 'fundraising'), ('general information', 'general information'), ('wedding/pre-wedding', 'wedding/pre-wedding'), ('hood personnel', 'hood personnel')], max_length=200)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('hood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nhood_app.neighbourhood')),
                ('owner', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='nhood_app.profile')),
            ],
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hood', to='nhood_app.profile'),
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('brief', models.TextField(blank=True, max_length=500)),
                ('emails', models.EmailField(max_length=200)),
                ('hood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nhood_app.neighbourhood')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nhood_app.profile')),
            ],
        ),
    ]