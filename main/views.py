from django.shortcuts import render, Http404, redirect
from .models import Tweet
from data.convert import text2png
import time
import os
from django.conf import settings


BASE_DIR = settings.BASE_DIR
BASE_URL = "127.0.0.1:8000/"
FONT_URL = os.path.join(BASE_DIR, "data/resources/font.ttf")


def index(request):
	return render(request, "index.html", locals())


def add(request):
	if request.method == "POST":
		if "tweetext" in request.POST:
			tweetext = request.POST["tweetext"]
			if len(tweetext)>0:
				tweetname = "tweet_"+str(time.time())
				tweeturl = "tweets/"+tweetname+".png"
				save_dir = os.path.join(BASE_DIR, "data/resources/tweets")
				save_dir = save_dir+"/"+tweetname+".png"
				tweet = Tweet.objects.create(content=tweetext, name=tweetname, url=tweeturl)
				text2png(tweetext, save_dir, fontfullpath = FONT_URL)
				tweet.save()
				return serve(request, tweet.id)
	return render(request, "add.html", locals())


def serve(request, tweetID):
	try:
		tweet = Tweet.objects.get(id=tweetID)
	except Tweet.ObjectNotFound:
		return Http404
	return redirect(absoluteURL(tweet))

######### HELPERS #############
def absoluteURL(tweet):
	return "http://" + BASE_URL + "data/resources/" + tweet.url