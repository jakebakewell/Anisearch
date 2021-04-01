from django.db import models
from login_reg_app.models import User
import re

class AnimeManager(models.Manager):
    def url_validator(self, post_data):
        search_errors = {}
        URL_REGEX = re.compile(r'^https?://(?:[a-zA-Z0-9\-]+\.)+[a-zA-Z0-9]{2,6}(?:/[^/#?]+)+\.(?:jpg|gif|png)$')
        if not URL_REGEX.match(post_data['search_img_url']):
            search_errors['url'] = "Invalid image/gif URL."
        return search_errors
    def update_validator(self, post_data):
        update_errors = {}
        if len(post_data['username']) < 1:
            update_errors['update_username'] = "Must enter username."
        if len(post_data['password']) < 1:
            update_errors['update_password'] = "Must enter password."
        if not post_data['password'] == post_data['password_confirm']:
            update_errors["update_password_confirm"] = "Passwords must match."
        return update_errors

class Anime(models.Model):
    user = models.ForeignKey(User, related_name="shows", on_delete = models.CASCADE)
    filename = models.CharField(max_length=255)
    tokenthumb = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    title_jp = models.CharField(max_length=255)
    genres = models.CharField(max_length=255)
    cover_image = models.URLField(max_length=255)
    at_time = models.FloatField()
    from_time = models.FloatField()
    to_time = models.FloatField()
    mal_id = models.IntegerField()
    anilist_id = models.IntegerField()
    mal_link = models.URLField(max_length=255)
    anilist_link = models.URLField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AnimeManager()