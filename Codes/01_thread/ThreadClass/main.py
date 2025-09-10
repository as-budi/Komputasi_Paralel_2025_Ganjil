"""calculating squared sum in thread"""

import time
import threading

def calculate_sum_squares(n):
    """Calculating sum of squares"""
    sum_squares = 0
    for i in range(n):
        sum_squares += i ** 2
    print(sum_squares)

def sleep_a_little(seconds):
    """Take a nap for seconds"""
    time.sleep(seconds)

def main():
    """Main function"""
    calc_start_time = time.time()

    current_threads = []
    for i in range(10):
        maximum_value = (i + 1) * 1000000
        t = threading.Thread(target=calculate_sum_squares, args=(maximum_value, ))
        t.start()
        current_threads.append(t)
        # calculate_sum_squares(maximum_value)

    for t in current_threads:
        t.join()

    print(f"Calculating sum of squares took: {time.time() - calc_start_time}")

    sleep_start_time = time.time()

    current_threads = []
    for seconds in range(1, 6):
        t = threading.Thread(target=sleep_a_little, args=(seconds, ))
        t.start()
        current_threads.append(t)
        # sleep_a_little(seconds)

    for t in current_threads:
        t.join()

    print(f"Sleep took: {time.time() - sleep_start_time}")

if __name__ == '__main__':
    main()