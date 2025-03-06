import threading
import queue
import time

def proceed_task(thread_nb,tasks_queue):
    while True:
        task = tasks_queue.get() #pobieramy zadania kolejki
        if task is None:
            break

        print(f'Wątek {thread_nb} przetwarza zadanie: {task}')
        time.sleep(1)
        tasks_queue.task_done()

queue_ = queue.Queue()
threads_ = 3

threads =[]


for i in range(threads_):
    thread = threading.Thread(target=proceed_task,args=(i,queue_))
    thread.start()
    threads.append(thread)


tasks = ['Zadanie A','Zadanie C','Zadanie C','Zadanie D','Zadanie E']

for tsk in tasks:
    queue_.put(tsk)

queue_.join()

for _ in range(threads_):
    queue_.put(None)

for th in threads:
    th.join()

print("wszystkie wątki zostały przetworzone!")
