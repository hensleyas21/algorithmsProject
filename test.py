import main
import time

# messing around with stuff

if __name__ == '__main__':
    a = main.random_list(10000000)
    start_time = time.time()
    lis = main.binary_search_lis(a)
    runtime_naive = time.time() - start_time
    print(f'Binary Search Solution:\n{lis}\nLength: {len(lis)}\n{runtime_naive:.2f} sec')