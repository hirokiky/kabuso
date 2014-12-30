# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', default=False, verbose_name='superuser status')),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, max_length=30, verbose_name='username', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')])),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=75, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(help_text='Designates whether the user can log into this admin site.', default=False, verbose_name='staff status')),
                ('is_active', models.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True, verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', to='auth.Group', related_query_name='user', verbose_name='groups', blank=True, related_name='user_set')),
                ('user_permissions', models.ManyToManyField(help_text='Specific permissions for this user.', to='auth.Permission', related_query_name='user', verbose_name='user permissions', blank=True, related_name='user_set')),
            ],
            options={
                'verbose_name_plural': 'users',
                'swappable': 'AUTH_USER_MODEL',
                'db_table': 'user',
                'verbose_name': 'user',
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
            ],
            options={
                'db_table': 'down_vote',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EarnedAchievement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('followee', models.ForeignKey(related_name='followees', to=settings.AUTH_USER_MODEL)),
                ('follower', models.ForeignKey(related_name='followers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'follow',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('page', models.ForeignKey(related_name='reads', to='core.Page')),
                ('user', models.ForeignKey(related_name='reads', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'read',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UpVote',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('page', models.ForeignKey(related_name='up_votes', to='core.Page')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'up_vote',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='upvote',
            unique_together=set([('user', 'page')]),
        ),
        migrations.AlterUniqueTogether(
            name='read',
            unique_together=set([('user', 'page')]),
        ),
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together=set([('followee', 'follower')]),
        ),
        migrations.AddField(
            model_name='downvote',
            name='page',
            field=models.ForeignKey(related_name='down_votes', to='core.Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='downvote',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='downvote',
            unique_together=set([('user', 'page')]),
        ),
        migrations.AddField(
            model_name='comment',
            name='page',
            field=models.ForeignKey(related_name='comments', to='core.Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(related_name='comments', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together=set([('user', 'page')]),
        ),
    ]
