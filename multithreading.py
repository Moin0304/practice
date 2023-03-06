import threading

# Function that will be executed on each thread
def worker(start, end):
    for i in range(start, end):
        # Do some computation here
        pass

# Number of threads to create
num_threads = 4

# Size of the task to be divided among the threads
task_size = 1000000

# Create and start each thread
threads = []
for i in range(num_threads):
    start = int(i * task_size / num_threads)
    end = int((i + 1) * task_size / num_threads)
    thread = threading.Thread(target=worker, args=(start, end))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print(worker(1,10))