from lxml import html
import requests
from urlparse import urljoin
import urlparse

# config

# url of the page containing song list
song_list_url = "http://www.songspk.link/audio_single_mp3_songs.html"

# base url used to resolve relative urls
base_url = "http://www.songspk.link/"

# song list -> song page -> mp3

def is_absolute(url):
	return bool(urlparse.urlparse(url).netloc)


# get list of song page urls

page = requests.get(song_list_url)
tree = html.fromstring(page.text)
links = tree.xpath('//a[@class="link"]/@href')

top_links = []
top_relative_links = []

for link in links:
	if is_absolute(link):
		top_links.append(link)
	else:
		# print link
		top_relative_links.append(link)


# get mp3 urls from song page urls

mp3_links = []

def get_mp3_url_from_page (link):
	page = requests.get(link)
	tree = html.fromstring(page.text)
	try:
		url = tree.xpath('//td[@class="Bitrate-td-2"]/a/@href')[0]
	except Exception, e:
		try:
			url = tree.xpath('//div[@class="song-title-bold"]/b/a/@href')[1]
		except Exception, e:
			print e
	return url

def get_mp3_url(mp3_page_urls):
	for link in mp3_page_urls:

		if not is_absolute(link):
			link = urljoin(base_url,link)

		try:
			url = get_mp3_url_from_page(link)
			print url
			mp3_links.append (url)
			pass
		except Exception, e:
			print e

	print len(mp3_links), "songs link fetched."

get_mp3_url(top_relative_links)