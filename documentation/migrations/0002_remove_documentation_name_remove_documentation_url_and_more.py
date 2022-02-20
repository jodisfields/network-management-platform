# Generated by Django 4.0.2 on 2022-02-20 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentation',
            name='name',
        ),
        migrations.RemoveField(
            model_name='documentation',
            name='url',
        ),
        migrations.AddField(
            model_name='documentation',
            name='category',
            field=models.CharField(default='Uncatagorized', help_text='Documentation Category.', max_length=255, verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='documentation',
            name='obj_url',
            field=models.URLField(default='Uncatagorized', help_text='Objective Reference.', max_length=255, verbose_name='URL'),
        ),
        migrations.AddField(
            model_name='documentation',
            name='title',
            field=models.CharField(default=None, help_text='Document Title.', max_length=255, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='documentation',
            name='description',
            field=models.TextField(blank=True, help_text='Documentation Description.', null=True, verbose_name='Description'),
        ),
    ]