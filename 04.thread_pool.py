import time
import threading
import blog_spider
import concurrent.futures

# crawl
with concurrent.futures.ThreadPoolExecutor() as pool:
	htmls = pool.map(blog_spider.crawl_2, blog_spider.urls)
	htmls = list(zip(blog_spider.urls, htmls))
	for url, html in htmls:
		print(url, len(html))
	
print("crawl over")

# prase
with concurrent.futures.ThreadPoolExecutor() as pool:
	futures = {}
	for url, html in htmls:
		future = pool.submit(blog_spider.parse, html)
		futures[future] = url
	# for future, url in futures.items():
	# 	print(url, future.result())
	
	for future in concurrent.futures.as_completed(futures):
		url = futures[future]
		print(url, future.result())
		



