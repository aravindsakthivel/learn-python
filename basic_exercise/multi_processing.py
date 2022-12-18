from multiprocessing import Process
import os
import time


def square_num():
	for num in range(100):
		num * num
		time.sleep(0.1)


# while using process use it inside a function
def main():
	processes = []
	num_process = os.cpu_count()

	print(num_process)

	for i in range(num_process):
		p = Process(target=square_num)
		p.start()
		processes.append(p)

	# join , use this to block main thread until process done
	for p in processes:
		p.join()

	print("Process over")


if __name__ == '__main__':
	main()


# multiprocessing GPT

# import multiprocessing
#
# def worker():
#     # Worker code goes here
#     print("Running worker process")
#
# if __name__ == '__main__':
#     # Create a new worker process
#     process = iprocessing.Process(target=worker)
#
#     # Start the worker process
#     process.start()
