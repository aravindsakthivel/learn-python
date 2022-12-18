from threading import Thread
import os
import time


def square_num():
	for num in range(100):
		num * num
		time.sleep(0.1)


threads = []
num_threads = 10

for i in range(num_threads):
	t = Thread(target=square_num)
	threads.append(t)

for t in threads:
	t.start()

# join , use this to block main thread until process done
for t in threads:
	t.join()

print("Thread over")
