from django.shortcuts import render, redirect

import requests
from bs4 import BeautifulSoup as BSoup
from news.models import Article

# Create your views here.

def scrape(request):
	if len(Article.objects.all()) > 500:
		Article.objects.all().delete()
	session = requests.Session()
	session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
	url = "https://www.gazeta.pl/0,0.html"

	# Store the webpage or response given by the server in content variable.
	content = session.get(url, verify=False).content

	# Create a soup object where we pass the HTML page. Also pass HTML parser as a parameter.
	soup = BSoup(content, "html.parser")

	News = soup.find_all('a', {"class":"article"})
	i = 0
	print('SPRAWDZAMMMMMM')
	print(News)
	for article in News:
		print(i)
		i = i + 1
		main = article.find('img')
		link = article['href']
		print(link)
		image = article.find('img')
		print(image)
		if image.has_key('data-src'):
			image_src = image['data-src']
		else:
			image_src = image['src']
		print(image_src)
		title = article['title']
		print(title)
		new_article = Article()
		new_article.title = title
		new_article.url = link
		new_article.image = image_src
		new_article.save()
	return redirect("../")


def news_list(request):


	articles = Article.objects.order_by('?')[:10]
	context = {
		'object_list': articles,
	}


	return render(request, "news/home.html", context)