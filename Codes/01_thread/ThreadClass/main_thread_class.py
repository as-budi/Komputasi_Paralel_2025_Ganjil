"""calculating squared sum in thread"""

import time
from SquareSumWorkers.square_sum_workers import SquaredSumWorkers
from SquareSumWorkers.sleepy_workers import SleepyWorker

def main():
    """Main function"""
    calc_start_time = time.time()

    current_workers = []
    for i in range(10):
        maximum_value = (i + 1) * 1000000
        squared_sum_worker = SquaredSumWorkers(n=maximum_value)
        current_workers.append(squared_sum_worker)

    for w in current_workers:
        w.join()

    print(f"Calculating sum of squares took: {time.time() - calc_start_time}")

    sleep_start_time = time.time()

    current_workers = []
    for seconds in range(1, 6):
        sleepy_worker = SleepyWorker(seconds=seconds)
        current_workers.append(sleepy_worker)

    for w in current_workers:
        w.join()
    print(f"Sleep took: {time.time() - sleep_start_time}")

if __name__ == '__main__':
    main()