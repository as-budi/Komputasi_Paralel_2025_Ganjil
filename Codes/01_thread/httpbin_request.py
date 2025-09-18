import time
import requests

urls = [
    'https://httpbin.org/delay/1',
    'https://httpbin.org/delay/2',
    'https://httpbin.org/delay/3',
]

start_time = time.time()
for url in urls:
    print(f'Starting request for {url}')
    response = requests.get(url)
    print(f'Fetched {url} with status code {response.status_code}')

end_time = time.time()
print(f'Total time taken: {end_time - start_time} seconds') 