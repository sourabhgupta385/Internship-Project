# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from .models import RssLinks
import feedparser
import email
import datetime
# Create your views here.

def index(request):
	data = RssLinks.objects.all()
	rss_links = []
	rss_links.extend(RssLinks.objects.values_list('link', flat=True).filter(category="Top Stories"))
	feedss = []
	prov =[]
	cat = []
	for url in rss_links:
		prov.append(RssLinks.objects.get(link=url).provider)
		cat.append(RssLinks.objects.get(link=url).category)
		feedss.append(feedparser.parse(url))
	final_provider = []
	final_category = []
	posttitle=[]
	postlink=[]
	postpublish=[]
	wer = 0
	for feed in feedss:
		for post in feed.entries:
			t=datetime.datetime.fromtimestamp(email.Utils.mktime_tz(email.Utils.parsedate_tz(post.published)))
			a = datetime.datetime.now() - t
			if a.total_seconds() < 3*3600:
				final_provider.append(prov[wer])
				final_category.append(cat[wer])
				posttitle.append(post.title)
				postlink.append(post.link)
				postpublish.append(t)
		wer = wer + 1
	zipped_data = zip(final_category , final_provider , postlink , posttitle ,postpublish)
	zipped_data.sort(key = lambda t: t[4],reverse = True)
	template = loader.get_template('intern/index.html')
	context = {'zipped_data':zipped_data,}
	return HttpResponse(template.render(context, request))

def bollywood(request):
	data = RssLinks.objects.all()
	rss_links = []
	rss_links.extend(RssLinks.objects.values_list('link', flat=True).filter(category="Bollywood"))
	feedss = []
	prov =[]
	cat = []
	for url in rss_links:
		prov.append(RssLinks.objects.get(link=url).provider)
		cat.append(RssLinks.objects.get(link=url).category)
		feedss.append(feedparser.parse(url))
	final_provider = []
	final_category = []
	posttitle=[]
	postlink=[]
	postpublish=[]
	wer = 0
	for feed in feedss:
		for post in feed.entries:
			t=datetime.datetime.fromtimestamp(email.Utils.mktime_tz(email.Utils.parsedate_tz(post.published)))
			a = datetime.datetime.now() - t
			if a.total_seconds() < 3*3600:
				final_provider.append(prov[wer])
				final_category.append(cat[wer])
				posttitle.append(post.title)
				postlink.append(post.link)
				postpublish.append(t)
		wer = wer + 1
	zipped_data = zip(final_category , final_provider , postlink , posttitle ,postpublish)
	zipped_data.sort(key = lambda t: t[4],reverse = True)
	template = loader.get_template('intern/bollywood.html')
	context = {'zipped_data':zipped_data,}
	return HttpResponse(template.render(context, request))			

def business(request):
	data = RssLinks.objects.all()
	rss_links = []
	rss_links.extend(RssLinks.objects.values_list('link', flat=True).filter(category="Business"))
	feedss = []
	prov =[]
	cat = []
	for url in rss_links:
		prov.append(RssLinks.objects.get(link=url).provider)
		cat.append(RssLinks.objects.get(link=url).category)
		feedss.append(feedparser.parse(url))
	final_provider = []
	final_category = []
	posttitle=[]
	postlink=[]
	postpublish=[]
	wer = 0
	for feed in feedss:
		for post in feed.entries:
			t=datetime.datetime.fromtimestamp(email.Utils.mktime_tz(email.Utils.parsedate_tz(post.published)))
			a = datetime.datetime.now() - t
			if a.total_seconds() < 3*3600:
				final_provider.append(prov[wer])
				final_category.append(cat[wer])
				posttitle.append(post.title)
				postlink.append(post.link)
				postpublish.append(t)
		wer = wer + 1
	zipped_data = zip(final_category , final_provider , postlink , posttitle ,postpublish)
	zipped_data.sort(key = lambda t: t[4],reverse = True)
	template = loader.get_template('intern/business.html')
	context = {'zipped_data':zipped_data,}
	return HttpResponse(template.render(context, request))

def education(request):
	data = RssLinks.objects.all()
	rss_links = []
	rss_links.extend(RssLinks.objects.values_list('link', flat=True).filter(category="Education"))
	feedss = []
	prov =[]
	cat = []
	for url in rss_links:
		prov.append(RssLinks.objects.get(link=url).provider)
		cat.append(RssLinks.objects.get(link=url).category)
		feedss.append(feedparser.parse(url))
	final_provider = []
	final_category = []
	posttitle=[]
	postlink=[]
	postpublish=[]
	wer = 0
	for feed in feedss:
		for post in feed.entries:
			t=datetime.datetime.fromtimestamp(email.Utils.mktime_tz(email.Utils.parsedate_tz(post.published)))
			a = datetime.datetime.now() - t
			if a.total_seconds() < 3*3600:
				final_provider.append(prov[wer])
				final_category.append(cat[wer])
				posttitle.append(post.title)
				postlink.append(post.link)
				postpublish.append(t)
		wer = wer + 1
	zipped_data = zip(final_category , final_provider , postlink , posttitle ,postpublish)
	zipped_data.sort(key = lambda t: t[4],reverse = True)
	template = loader.get_template('intern/education.html')
	context = {'zipped_data':zipped_data,}
	return HttpResponse(template.render(context, request))

def entertainment(request):
	data = RssLinks.objects.all()
	rss_links = []
	rss_links.extend(RssLinks.objects.values_list('link', flat=True).filter(category="Entertainment"))
	feedss = []
	prov =[]
	cat = []
	for url in rss_links:
		prov.append(RssLinks.objects.get(link=url).provider)
		cat.append(RssLinks.objects.get(link=url).category)
		feedss.append(feedparser.parse(url))
	final_provider = []
	final_category = []
	posttitle=[]
	postlink=[]
	postpublish=[]
	wer = 0
	for feed in feedss:
		for post in feed.entries:
			t=datetime.datetime.fromtimestamp(email.Utils.mktime_tz(email.Utils.parsedate_tz(post.published)))
			a = datetime.datetime.now() - t
			if a.total_seconds() < 3*3600:
				final_provider.append(prov[wer])
				final_category.append(cat[wer])
				posttitle.append(post.title)
				postlink.append(post.link)
				postpublish.append(t)
		wer = wer + 1
	zipped_data = zip(final_category , final_provider , postlink , posttitle ,postpublish)
	zipped_data.sort(key = lambda t: t[4],reverse = True)
	template = loader.get_template('intern/entertainment.html')
	context = {'zipped_data':zipped_data,}
	return HttpResponse(template.render(context, request))

def health(request):
	data = RssLinks.objects.all()
	rss_links = []
	rss_links.extend(RssLinks.objects.values_list('link', flat=True).filter(category="Health"))
	feedss = []
	prov =[]
	cat = []
	for url in rss_links:
		prov.append(RssLinks.objects.get(link=url).provider)
		cat.append(RssLinks.objects.get(link=url).category)
		feedss.append(feedparser.parse(url))
	final_provider = []
	final_category = []
	posttitle=[]
	postlink=[]
	postpublish=[]
	wer = 0
	for feed in feedss:
		for post in feed.entries:
			t=datetime.datetime.fromtimestamp(email.Utils.mktime_tz(email.Utils.parsedate_tz(post.published)))
			a = datetime.datetime.now() - t
			if a.total_seconds() < 3*3600:
				final_provider.append(prov[wer])
				final_category.append(cat[wer])
				posttitle.append(post.title)
				postlink.append(post.link)
				postpublish.append(t)
		wer = wer + 1
	zipped_data = zip(final_category , final_provider , postlink , posttitle ,postpublish)
	zipped_data.sort(key = lambda t: t[4],reverse = True)
	template = loader.get_template('intern/health.html')
	context = {'zipped_data':zipped_data,}
	return HttpResponse(template.render(context, request))


def india(request):
	data = RssLinks.objects.all()
	rss_links = []
	rss_links.extend(RssLinks.objects.values_list('link', flat=True).filter(category="India"))
	feedss = []
	prov =[]
	cat = []
	for url in rss_links:
		prov.append(RssLinks.objects.get(link=url).provider)
		cat.append(RssLinks.objects.get(link=url).category)
		feedss.append(feedparser.parse(url))
	final_provider = []
	final_category = []
	posttitle=[]
	postlink=[]
	postpublish=[]
	wer = 0
	for feed in feedss:
		for post in feed.entries:
			t=datetime.datetime.fromtimestamp(email.Utils.mktime_tz(email.Utils.parsedate_tz(post.published)))
			a = datetime.datetime.now() - t
			if a.total_seconds() < 3*3600:
				final_provider.append(prov[wer])
				final_category.append(cat[wer])
				posttitle.append(post.title)
				postlink.append(post.link)
				postpublish.append(t)
		wer = wer + 1
	zipped_data = zip(final_category , final_provider , postlink , posttitle ,postpublish)
	zipped_data.sort(key = lambda t: t[4],reverse = True)
	template = loader.get_template('intern/india.html')
	context = {'zipped_data':zipped_data,}
	return HttpResponse(template.render(context, request))

def lifestyle(request):
	data = RssLinks.objects.all()
	rss_links = []
	rss_links.extend(RssLinks.objects.values_list('link', flat=True).filter(category="Life Style"))
	feedss = []
	prov =[]
	cat = []
	for url in rss_links:
		prov.append(RssLinks.objects.get(link=url).provider)
		cat.append(RssLinks.objects.get(link=url).category)
		feedss.append(feedparser.parse(url))
	final_provider = []
	final_category = []
	posttitle=[]
	postlink=[]
	postpublish=[]
	wer = 0
	for feed in feedss:
		for post in feed.entries:
			t=datetime.datetime.fromtimestamp(email.Utils.mktime_tz(email.Utils.parsedate_tz(post.published)))
			a = datetime.datetime.now() - t
			if a.total_seconds() < 3*3600:
				final_provider.append(prov[wer])
				final_category.append(cat[wer])
				posttitle.append(post.title)
				postlink.append(post.link)
				postpublish.append(t)
		wer = wer + 1
	zipped_data = zip(final_category , final_provider , postlink , posttitle ,postpublish)
	zipped_data.sort(key = lambda t: t[4],reverse = True)
	template = loader.get_template('intern/lifestyle.html')
	context = {'zipped_data':zipped_data,}
	return HttpResponse(template.render(context, request))

def realstate(request):
	data = RssLinks.objects.all()
	rss_links = []
	rss_links.extend(RssLinks.objects.values_list('link', flat=True).filter(category="Real State"))
	feedss = []
	prov =[]
	cat = []
	for url in rss_links:
		prov.append(RssLinks.objects.get(link=url).provider)
		cat.append(RssLinks.objects.get(link=url).category)
		feedss.append(feedparser.parse(url))
	final_provider = []
	final_category = []
	posttitle=[]
	postlink=[]
	postpublish=[]
	wer = 0
	for feed in feedss:
		for post in feed.entries:
			t=datetime.datetime.fromtimestamp(email.Utils.mktime_tz(email.Utils.parsedate_tz(post.published)))
			a = datetime.datetime.now() - t
			if a.total_seconds() < 3*3600:
				final_provider.append(prov[wer])
				final_category.append(cat[wer])
				posttitle.append(post.title)
				postlink.append(post.link)
				postpublish.append(t)
		wer = wer + 1
	zipped_data = zip(final_category , final_provider , postlink , posttitle ,postpublish)
	zipped_data.sort(key = lambda t: t[4],reverse = True)
	template = loader.get_template('intern/realstate.html')
	context = {'zipped_data':zipped_data,}
	return HttpResponse(template.render(context, request))
		
def sports(request):
	data = RssLinks.objects.all()
	rss_links = []
	rss_links.extend(RssLinks.objects.values_list('link', flat=True).filter(category="Sports"))
	feedss = []
	prov =[]
	cat = []
	for url in rss_links:
		prov.append(RssLinks.objects.get(link=url).provider)
		cat.append(RssLinks.objects.get(link=url).category)
		feedss.append(feedparser.parse(url))
	final_provider = []
	final_category = []
	posttitle=[]
	postlink=[]
	postpublish=[]
	wer = 0
	for feed in feedss:
		for post in feed.entries:
			t=datetime.datetime.fromtimestamp(email.Utils.mktime_tz(email.Utils.parsedate_tz(post.published)))
			a = datetime.datetime.now() - t
			if a.total_seconds() < 3*3600:
				final_provider.append(prov[wer])
				final_category.append(cat[wer])
				posttitle.append(post.title)
				postlink.append(post.link)
				postpublish.append(t)
		wer = wer + 1
	zipped_data = zip(final_category , final_provider , postlink , posttitle ,postpublish)
	zipped_data.sort(key = lambda t: t[4],reverse = True)
	template = loader.get_template('intern/sports.html')
	context = {'zipped_data':zipped_data,}
	return HttpResponse(template.render(context, request))

def technology(request):
	data = RssLinks.objects.all()
	rss_links = []
	rss_links.extend(RssLinks.objects.values_list('link', flat=True).filter(category="Technology"))
	feedss = []
	prov =[]
	cat = []
	for url in rss_links:
		prov.append(RssLinks.objects.get(link=url).provider)
		cat.append(RssLinks.objects.get(link=url).category)
		feedss.append(feedparser.parse(url))
	final_provider = []
	final_category = []
	posttitle=[]
	postlink=[]
	postpublish=[]
	wer = 0
	for feed in feedss:
		for post in feed.entries:
			t=datetime.datetime.fromtimestamp(email.Utils.mktime_tz(email.Utils.parsedate_tz(post.published)))
			a = datetime.datetime.now() - t
			if a.total_seconds() < 3*3600:
				final_provider.append(prov[wer])
				final_category.append(cat[wer])
				posttitle.append(post.title)
				postlink.append(post.link)
				postpublish.append(t)
		wer = wer + 1
	zipped_data = zip(final_category , final_provider , postlink , posttitle ,postpublish)
	zipped_data.sort(key = lambda t: t[4],reverse = True)
	template = loader.get_template('intern/technology.html')
	context = {'zipped_data':zipped_data,}
	return HttpResponse(template.render(context, request))


def world(request):
	data = RssLinks.objects.all()
	rss_links = []
	rss_links.extend(RssLinks.objects.values_list('link', flat=True).filter(category="World"))
	feedss = []
	prov =[]
	cat = []
	for url in rss_links:
		prov.append(RssLinks.objects.get(link=url).provider)
		cat.append(RssLinks.objects.get(link=url).category)
		feedss.append(feedparser.parse(url))
	final_provider = []
	final_category = []
	posttitle=[]
	postlink=[]
	postpublish=[]
	wer = 0
	for feed in feedss:
		for post in feed.entries:
			t=datetime.datetime.fromtimestamp(email.Utils.mktime_tz(email.Utils.parsedate_tz(post.published)))
			a = datetime.datetime.now() - t
			if a.total_seconds() < 3*3600:
				final_provider.append(prov[wer])
				final_category.append(cat[wer])
				posttitle.append(post.title)
				postlink.append(post.link)
				postpublish.append(t)
		wer = wer + 1
	zipped_data = zip(final_category , final_provider , postlink , posttitle ,postpublish)
	zipped_data.sort(key = lambda t: t[4],reverse = True)
	template = loader.get_template('intern/world.html')
	context = {'zipped_data':zipped_data,}
	return HttpResponse(template.render(context, request))