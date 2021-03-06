# Generated by Django 2.1.5 on 2019-03-18 11:48

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
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('Lab Services', 'Lab Services'), ('Transport Services', 'Transport Services'), ('Waste Generator', 'Waste Generator'), ('Waste Treatment', 'Waste Treatment'), ('Waste Storage', 'Waste Storage')], default='Transport Services', max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authentication.Company')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
