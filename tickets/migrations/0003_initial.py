# Generated by Django 4.0.2 on 2022-02-20 10:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tickets', '0002_delete_tickets'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('title', models.CharField(default=None, help_text='Ticket Title', max_length=50, verbose_name='Title')),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'tickets',
                'verbose_name_plural': 'tickets',
                'db_table': 'tickets',
            },
        ),
    ]
