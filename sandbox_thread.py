import threading
import os
import concurrent.futures


# threading
def print_cube(size):
    print(f"Cube:{size * size * size}")
    print(f"Cube current thread id:{threading.current_thread().name}")
    print(f"Cube Process id:{os.getpid()}")


def print_square(size):
    print(f"Square:{size * size}")
    print(f"Square current thread id:{threading.current_thread().name}")
    print(f"Square Process id:{os.getpid()}")


print(f"Main Process id:{os.getpid()}")
print(f"Main current thread id:{threading.current_thread().name}")

t1 = threading.Thread(target=print_cube, args=(5,))
t2 = threading.Thread(target=print_square, args=(2,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Done")


# threadpool
def worker():
    print("Worker thread running")


pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)

pool.submit(worker)
pool.submit(worker)

pool.shutdown(wait=True)

print("Main thread continuing to run")
