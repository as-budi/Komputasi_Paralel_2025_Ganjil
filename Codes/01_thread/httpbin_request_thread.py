import time
import requests
import threading

urls = [
    'https://httpbin.org/delay/1',
    'https://httpbin.org/delay/2',
    'https://httpbin.org/delay/3',
]

def fetch_url(url):
    response = requests.get(url)
    print(f'Fetched {url} with status code {response.status_code}')

threads = []
start_time = time.time()
for url in urls:
    thread = threading.Thread(target=fetch_url, args=(url,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

end_time = time.time()
print(f'Total time taken: {end_time - start_time} seconds') 
