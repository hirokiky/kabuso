# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')], max_length=30, unique=True, verbose_name='username', help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.')),
                ('first_name', models.CharField(max_length=30, blank=True, verbose_name='first name')),
                ('last_name', models.CharField(max_length=30, blank=True, verbose_name='last name')),
                ('email', models.EmailField(max_length=75, blank=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status', help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(default=True, verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, related_query_name='user', related_name='user_set', verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', to='auth.Group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_query_name='user', related_name='user_set', verbose_name='user permissions', help_text='Specific permissions for this user.', to='auth.Permission')),
            ],
            options={
                'verbose_name_plural': 'users',
                'db_table': 'user',
                'swappable': 'AUTH_USER_MODEL',
                'abstract': False,
                'verbose_name': 'user',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('updated_at', models.DateTimeField(db_index=True, auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('point', models.IntegerField()),
            ],
            options={
                'db_table': 'achievement',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('updated_at', models.DateTimeField(db_index=True, auto_now=True)),
                ('body', models.TextField(max_length=4095)),
            ],
            options={
                'db_table': 'comment',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DownVote',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('updated_at', models.DateTimeField(db_index=True, auto_now=True)),
                ('comment', models.ForeignKey(to='core.Comment', related_name='down_votes')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'down_vote',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EarnedAchievement',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('updated_at', models.DateTimeField(db_index=True, auto_now=True)),
                ('achievement', models.ForeignKey(to='core.Achievement')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'earned_achievement',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('updated_at', models.DateTimeField(db_index=True, auto_now=True)),
                ('followee', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='followees')),
                ('follower', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='followers')),
            ],
            options={
                'db_table': 'follow',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('updated_at', models.DateTimeField(db_index=True, auto_now=True)),
                ('page_url', models.URLField(unique=True)),
                ('title', models.CharField(max_length=255)),
                ('summary_image_url', models.URLField()),
                ('summary', models.TextField(max_length=4095)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'page',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Read',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('updated_at', models.DateTimeField(db_index=True, auto_now=True)),
                ('page', models.ForeignKey(to='core.Page', related_name='reads')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='reads')),
            ],
            options={
                'db_table': 'read',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UpVote',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('updated_at', models.DateTimeField(db_index=True, auto_now=True)),
                ('comment', models.ForeignKey(to='core.Comment', related_name='up_votes')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'up_vote',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='upvote',
            unique_together=set([('user', 'comment')]),
        ),
        migrations.AlterUniqueTogether(
            name='read',
            unique_together=set([('user', 'page')]),
        ),
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together=set([('followee', 'follower')]),
        ),
        migrations.AlterUniqueTogether(
            name='downvote',
            unique_together=set([('user', 'comment')]),
        ),
        migrations.AddField(
            model_name='comment',
            name='page',
            field=models.ForeignKey(to='core.Page', related_name='comments'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='comments'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together=set([('user', 'page')]),
        ),
    ]
