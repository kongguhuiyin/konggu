import threading
import time

lock = threading.Lock()

class Account:
	def __init__(self, balance):
		self.balance = balance

def draw(account, amount):
	with lock:   # 第一个线程加锁之后会让第二个线程无法执行锁内部结构
		if account.balance >= amount:
			time.sleep(0.1)    # sleep语句会导致线程阻塞并切换线程
			print(threading.current_thread().name, "取钱成功")
			account.balance -= amount
			print(threading.current_thread().name, "余额", account.balance)
		else:
			print(threading.current_thread().name, "取钱失败，余额不足")


if __name__ == "__main__":
	account = Account(1000)
	ta = threading.Thread(name='ta', target=draw, args=(account, 800))
	tb = threading.Thread(name='tb', target=draw, args=(account, 800))
	
	ta.start()
	tb.start()
