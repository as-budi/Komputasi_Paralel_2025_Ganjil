import threading
import time

def tugas(nama):
    for i in range(5):
        print(f'Tugas {nama} ke-{i+1}')
        time.sleep(1)

start_time = time.time()
thread1 = threading.Thread(target=tugas, args=('A',))
thread2 = threading.Thread(target=tugas, args=('B',))
thread3 = threading.Thread(target=tugas, args=('C',))
thread4 = threading.Thread(target=tugas, args=('D',))

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
# tugas('A')
# tugas('B')
end_time = time.time()
print(f'Waktu eksekusi: {end_time - start_time} detik')