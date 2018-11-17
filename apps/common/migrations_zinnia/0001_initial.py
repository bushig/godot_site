# Generated by Django 2.0.9 on 2018-11-17 00:17

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mptt.fields
import tagging.fields
import zinnia.models_bases.entry


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', models.SlugField(help_text="Used to build the category's URL.", max_length=255, unique=True, verbose_name='slug')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='zinnia.Category', verbose_name='parent category')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', models.SlugField(help_text="Used to build the entry's URL.", max_length=255, unique_for_date='publication_date', verbose_name='slug')),
                ('status', models.IntegerField(choices=[(0, 'draft'), (1, 'hidden'), (2, 'published')], db_index=True, default=0, verbose_name='status')),
                ('publication_date', models.DateTimeField(db_index=True, default=django.utils.timezone.now, help_text="Used to build the entry's URL.", verbose_name='publication date')),
                ('start_publication', models.DateTimeField(blank=True, db_index=True, help_text='Start date of publication.', null=True, verbose_name='start publication')),
                ('end_publication', models.DateTimeField(blank=True, db_index=True, help_text='End date of publication.', null=True, verbose_name='end publication')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='creation date')),
                ('last_update', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last update')),
                ('content', models.TextField(blank=True, verbose_name='content')),
                ('comment_enabled', models.BooleanField(default=True, help_text='Allows comments if checked.', verbose_name='comments enabled')),
                ('pingback_enabled', models.BooleanField(default=True, help_text='Allows pingbacks if checked.', verbose_name='pingbacks enabled')),
                ('trackback_enabled', models.BooleanField(default=True, help_text='Allows trackbacks if checked.', verbose_name='trackbacks enabled')),
                ('comment_count', models.IntegerField(default=0, verbose_name='comment count')),
                ('pingback_count', models.IntegerField(default=0, verbose_name='pingback count')),
                ('trackback_count', models.IntegerField(default=0, verbose_name='trackback count')),
                ('lead', models.TextField(blank=True, help_text='Lead paragraph', verbose_name='lead')),
                ('excerpt', models.TextField(blank=True, help_text='Used for SEO purposes.', verbose_name='excerpt')),
                ('image', models.ImageField(blank=True, help_text='Used for illustration.', upload_to=zinnia.models_bases.entry.image_upload_to_dispatcher, verbose_name='image')),
                ('image_caption', models.TextField(blank=True, help_text="Image's caption.", verbose_name='caption')),
                ('featured', models.BooleanField(default=False, verbose_name='featured')),
                ('tags', tagging.fields.TagField(blank=True, max_length=255, verbose_name='tags')),
                ('login_required', models.BooleanField(default=False, help_text='Only authenticated users can view the entry.', verbose_name='login required')),
                ('password', models.CharField(blank=True, help_text='Protects the entry with a password.', max_length=50, verbose_name='password')),
                ('content_template', models.CharField(choices=[('zinnia/_entry_detail.html', 'Default template'), ('zinnia/_short_entry_detail.html', 'Short entry template')], default='zinnia/_entry_detail.html', help_text="Template used to display the entry's content.", max_length=250, verbose_name='content template')),
                ('detail_template', models.CharField(choices=[('entry_detail.html', 'Default template')], default='entry_detail.html', help_text="Template used to display the entry's detail page.", max_length=250, verbose_name='detail template')),
            ],
            options={
                'verbose_name': 'entry',
                'verbose_name_plural': 'entries',
                'ordering': ['-publication_date'],
                'permissions': (('can_view_all', 'Can view all entries'), ('can_change_status', 'Can change status'), ('can_change_author', 'Can change author(s)')),
                'get_latest_by': 'publication_date',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('auth.user', models.Model),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='authors',
            field=models.ManyToManyField(blank=True, related_name='entries', to='zinnia.Author', verbose_name='authors'),
        ),
        migrations.AddField(
            model_name='entry',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='entries', to='zinnia.Category', verbose_name='categories'),
        ),
        migrations.AddField(
            model_name='entry',
            name='related',
            field=models.ManyToManyField(blank=True, related_name='_entry_related_+', to='zinnia.Entry', verbose_name='related entries'),
        ),
        migrations.AddField(
            model_name='entry',
            name='sites',
            field=models.ManyToManyField(help_text='Sites where the entry will be published.', related_name='entries', to='sites.Site', verbose_name='sites'),
        ),
        migrations.AlterIndexTogether(
            name='entry',
            index_together={('slug', 'publication_date'), ('status', 'publication_date', 'start_publication', 'end_publication')},
        ),
    ]
