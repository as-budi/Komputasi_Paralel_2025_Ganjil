import threading
import time

def tugas(nama):
    for i in range(5):
        print(f'Tugas {nama} ke-{i+1}')
        time.sleep(10)

start_time = time.time()
thread1 = threading.Thread(target=tugas, args=('A',))
thread2 = threading.Thread(target=tugas, args=('B',))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
# tugas('A')
# tugas('B')
end_time = time.time()
print(f'Waktu eksekusi: {end_time - start_time} detik')