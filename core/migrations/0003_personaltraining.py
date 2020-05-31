# Generated by Django 3.0.3 on 2020-05-31 12:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_auto_20200315_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalTraining',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('location_name', models.CharField(blank=True, max_length=255, null=True)),
                ('lon', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('lat', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('terms', models.TextField()),
                ('is_onsite', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('gym_member', models.ForeignKey(limit_choices_to={'role', 'Member'}, on_delete=django.db.models.deletion.CASCADE, related_name='member_personal_trainings', to=settings.AUTH_USER_MODEL)),
                ('gym_trainer', models.ForeignKey(limit_choices_to={'role', 'Trainer'}, on_delete=django.db.models.deletion.CASCADE, related_name='trainer_personal_trainings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]