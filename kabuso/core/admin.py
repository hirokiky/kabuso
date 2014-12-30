from django.contrib import admin

from core import models


admin.site.register((
    models.User,
    models.Page,
    models.Comment,
    models.Achievement,
))
