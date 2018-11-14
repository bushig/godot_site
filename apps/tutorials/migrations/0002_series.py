# Generated by Django 2.0.9 on 2018-11-12 02:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import image_cropping.fields
import markdownx.models
import tagulous.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0001_initial'),
        ('assets', '0001_initial'),
        ('frameworks', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tutorials', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('short_description', models.CharField(blank=True, max_length=500)),
                ('content', markdownx.models.MarkdownxField(blank=True)),
                ('credit_note', models.CharField(blank=True, max_length=255)),
                ('image', image_cropping.fields.ImageCropField(blank=True, upload_to='uploaded_images')),
                ('cropping', image_cropping.fields.ImageRatioField('image', '300x300', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('assets', models.ManyToManyField(blank=True, related_name='series', to='assets.Asset')),
                ('frameworks', models.ManyToManyField(blank=True, related_name='series', to='frameworks.Framework')),
                ('languages', models.ManyToManyField(blank=True, related_name='series', to='languages.Language')),
                ('tags', tagulous.models.fields.TagField(_set_tag_meta=True, force_lowercase=True, help_text='Enter a comma-separated tag string', space_delimiter=False, to='tutorials.Tagulous_Tutorial_tags', tree=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('users_liked', models.ManyToManyField(blank=True, related_name='series_liked', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
