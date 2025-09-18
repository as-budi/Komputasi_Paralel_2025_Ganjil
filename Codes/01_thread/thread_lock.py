import threading

saldo = 0
lock = threading.Lock()

def tambah_saldo(angka):
    global saldo
    for _ in range(100000):
        lock.acquire()
        saldo += angka
        lock.release()

def kurangi_saldo(angka):
    global saldo
    for _ in range(100000):
        lock.acquire()
        saldo -= angka
        lock.release()

t1=[]
t2=[]
for _ in range(10):
    t = threading.Thread(target=tambah_saldo, args=(5,))
    t.start()
    t1.append(t)

for _ in range(10):
    t = threading.Thread(target=kurangi_saldo, args=(5,))
    t.start()
    t2.append(t)
# t2 = threading.Thread(target=kurangi_saldo, args=(5,))

# t1.start()
# t2.start()

for t in t1:
    t.join()
for t in t2:
    t.join()

print(f'Saldo akhir: {saldo}')