import time
import multiprocessing

start_time = time.perf_counter()
def sleep_for_abit(seconds):
    print(f'sleeping {seconds} seconds')
    time.sleep(seconds)
    print(f'done sleeping for {seconds}')


p1 = multiprocessing.Process(target=sleep_for_abit, args=[5])
p2 = multiprocessing.Process(target=sleep_for_abit, args=[2])

if __name__ == '__main__':
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    finish_time = time.perf_counter()
    print(f'Finished running after seconds {finish_time - start_time}')
