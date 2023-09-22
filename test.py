from time import sleep, perf_counter
from threading import Thread

import requests

def task():
    print('Starting a task...')
    url = "https://dados.cvm.gov.br/dados/FI/DOC/EVENTUAL/DADOS/eventual_fi_2023.csv"
    resp = requests.get(url)
    resp.raise_for_status()
    print('done', resp.ok)

start_time = perf_counter()

# create two new threads
t = [Thread(target=task) for i in range(10)]

for i in t:
    i.start()
for i in t:
    i.join()

end_time = perf_counter()

print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')

start_time = perf_counter()
[task() for i in range(10)]
end_time = perf_counter()
print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')
