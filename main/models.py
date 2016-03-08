from __future__ import unicode_literals

from django.db import models



class Tweet(models.Model):
	content = models.TextField(blank=True)
	name = models.CharField(max_length=225)
	url = models.CharField(max_length=225, null=True)
	created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return "tweet created at "+str(self.created)
