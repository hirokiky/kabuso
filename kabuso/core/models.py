from django.conf import settings
from django.contrib.auth import models as auth_models
from django.db import models
from django.utils import timezone


class User(auth_models.AbstractUser):
    class Meta(auth_models.AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class BaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']


class Follow(BaseModel):
    followee = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='followee')
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='follower')

    class Meta:
        db_table = 'follow'


class Page(BaseModel):
    page_url = models.URLField()
    title = models.CharField(max_length=255)
    summary_image_url = models.URLField()
    summary = models.TextField(max_length=4095)
    description = models.TextField()

    class Meta:
        db_table = 'page'


class Read(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    page = models.ForeignKey(Page)

    class Meta:
        db_table = 'read'


class Comment(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    page = models.ForeignKey(Page)
    body = models.TextField(max_length=4095)

    class Meta:
        db_table = 'comment'


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
    page = models.ForeignKey(Page)

    class Meta:
        db_table = 'up_vote'


class DownVote(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    page = models.ForeignKey(Page)

    class Meta:
        db_table = 'down_vote'
