import threading
import time

class MyThread(threading.Thread):
    def __init__(self, name, delay):
        super(MyThread, self).__init__()
        self.name = name
        self.delay = delay

    def run(self):
        print(f'Thread {self.name} starting')
        for i in range(5):
            print(f'Thread {self.name} working {i+1}')
            time.sleep(self.delay)
        print(f'Thread {self.name} finished')

start_time = time.time()
thread1 = MyThread(name='A', delay=1)
thread2 = MyThread(name='B', delay=1)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
end_time = time.time()
print(f'Waktu eksekusi: {end_time - start_time} detik')