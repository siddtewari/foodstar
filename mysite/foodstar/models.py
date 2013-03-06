from django.db import models

class foodlist(models.Model):
	title = models.CharField(max_length=200)
	created = models.DateTimeField('Date created')
	def __unicode__(self):
		return self.title

class fooditem(models.Model):
	flist = models.ForeignKey(foodlist)
	item = models.CharField(max_length=200)
	def __unicode__(self):
		return self.item
