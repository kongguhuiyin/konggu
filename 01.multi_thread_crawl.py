import blog_spider
import threading
import time
import queue



def single_thread():
	print("single_thread begin")
	for url in blog_spider.urls:
		blog_spider.crawl(url)
	print("single_thread end")
	

def multi_thread():
	print("multi_thread begin")
	threads = []
	for url in blog_spider.urls:
		threads.append(
			threading.Thread(target=blog_spider.crawl, args=(url,))
		)
	
	for thread in threads:
		thread.start()
	
	for thread in threads:
		thread.join()

	print("multi_thread end")


if __name__ == "__main__":
	start = time.time()
	single_thread()
	end = time.time()
	print("single_thread time", end-start)
	
	start = time.time()
	multi_thread()
	end = time.time()
	print("multi_thread time", end - start)
	

