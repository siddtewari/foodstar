import datetime
from django.utils import timezone

from django.db import models

class Lists(models.Model):
	title = models.CharField(max_length=200)
	created = models.DateTimeField('date added')
	def __unicode__(self):
		return self.title

	def was_added_recently(self):
		return self.created >= timezone.now() - datetime.timedelta(days=1)
	was_added_recently.admin_order_field = 'created'
	was_added_recently.boolean = True
	was_added_recently.short_description = 'Added recently?'

class Items(models.Model):
	lists = models.ForeignKey(Lists)
	item = models.CharField(max_length=200)
	quantity = models.IntegerField()
	def __unicode__(self):
		return self.item