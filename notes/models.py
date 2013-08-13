from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

class Note(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    pub_date = models.DateTimeField('date published')
    cat = models.ForeignKey(Category)
    user = models.ForeignKey(User)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.title
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'