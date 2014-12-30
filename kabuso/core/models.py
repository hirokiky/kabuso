from django.conf import settings
from django.contrib.auth import models as auth_models
from django.db import models
from django.utils import timezone


class User(auth_models.AbstractUser):
    class Meta(auth_models.AbstractUser.Meta):
        db_table = 'user'
        swappable = 'AUTH_USER_MODEL'


class BaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']


class Follow(BaseModel):
    followee = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='followees')
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='followers')

    class Meta:
        db_table = 'follow'
        unique_together = ('followee', 'follower')


class Page(BaseModel):
    page_url = models.URLField(unique=True)
    title = models.CharField(max_length=255)
    summary_image_url = models.URLField()
    summary = models.TextField(max_length=4095)
    description = models.TextField()

    class Meta:
        db_table = 'page'


class Read(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reads')
    page = models.ForeignKey(Page, related_name='reads')

    class Meta:
        db_table = 'read'
        unique_together = ('user', 'page')


class Comment(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments')
    page = models.ForeignKey(Page, related_name='comments')
    body = models.TextField(max_length=4095)

    class Meta:
        db_table = 'comment'
        unique_together = ('user', 'page')


class Achievement(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()
    point = models.IntegerField()

    class Meta:
        db_table = 'achievement'


class EarnedAchievement(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    achievement = models.ForeignKey(Achievement)

    class Meta:
        db_table = 'earned_achievement'


class UpVote(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    comment = models.ForeignKey(Comment, related_name='up_votes')

    class Meta:
        db_table = 'up_vote'
        unique_together = ('user', 'comment')


class DownVote(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    comment = models.ForeignKey(Comment, related_name='down_votes')

    class Meta:
        db_table = 'down_vote'
        unique_together = ('user', 'comment')
