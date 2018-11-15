# Generated by Django 2.0.9 on 2018-11-14 01:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0003_auto_20181113_2322'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='series',
            options={'ordering': ['-updated'], 'verbose_name_plural': 'series'},
        ),
        migrations.AlterModelOptions(
            name='tutorialmembership',
            options={'ordering': ['order']},
        ),
        migrations.AlterUniqueTogether(
            name='tutorialmembership',
            unique_together={('tutorial', 'series')},
        ),
    ]