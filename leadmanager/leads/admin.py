# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Lead, link, movie, rating, tag, User

# Register your models here.

# Import Model into Admin
admin.site.register(Lead)
# Database
admin.site.register(link)
admin.site.register(movie)
admin.site.register(rating)
admin.site.register(tag)
admin.site.register(User)
