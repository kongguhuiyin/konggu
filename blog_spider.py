import requests as req
import threading
from bs4 import BeautifulSoup


urls = [f'https://www.cnblogs.com/p/{page}' for page in range(1, 50 + 1)]

def crawl(url):
	r = req.get(url)
	# print(url, len(r.text))


def crawl_2(url):
	r = req.get(url)
	return r.text

def parse(html):
	# class="post-item-title"
	soup = BeautifulSoup(html, "html.parser")
	links = soup.find_all("a", class_="post-item-title")
	return [(link['href'], link.get_text()) for link in links]


if __name__ == "__main__":
	# for res in parse(crawl_2(urls[1])):
	# 	print(res)
	# print(urls)
	for url in urls:
		t = crawl_2(url)
		print(len(t))
	