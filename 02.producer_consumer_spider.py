import blog_spider
import threading
import time
import queue
import random

def do_crawl(url_queue: queue.Queue, html_queue: queue.Queue):
	while True:
		url = url_queue.get()
		html = blog_spider.crawl_2(url)
		html_queue.put(html)
		# 当前线程名字，链接，大小
		print(threading.current_thread().name, f"crawl {url}", "url_queue.qsize =", url_queue.qsize())
		time.sleep(random.randint(1, 2))
		

def do_parse(html_queue: queue.Queue, fout):
	while True:
		html = html_queue.get()
		results = blog_spider.parse(html)
		for res in results:
			fout.write(str(res) + '\n')
		time.sleep(random.randint(1, 2))
		print(threading.current_thread().name, f"results.size", len(results), "html_queue.qsize =", html_queue.qsize())


if __name__=="__main__":
	url_queue = queue.Queue()
	html_queue = queue.Queue()
	
	for url in blog_spider.urls:
		url_queue.put(url)
	
	for idx in range(3):
		t = threading.Thread(target=do_crawl, args=(url_queue, html_queue), name=f"crawl{idx}")
		t.start()
	
	fout = open("02.data.txt", "w")
	for idx in range(3):
		t = threading.Thread(target=do_parse, args=(html_queue, fout), name=f"parse{idx}")
		t.start()
	



