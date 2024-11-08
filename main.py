import time
import random

def random_list(n: int) -> list[int]:
    return [random.randint(1, n) for _ in range(n)]

def naive_lis_recursive(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    
    max_lis = [arr[-1]]

    for i in range(len(arr)):
        if arr[i] < arr[-1]:
            lis_i = naive_lis_recursive(arr[:i+1])
            if len(max_lis) < len(lis_i) + 1:
                max_lis = lis_i
    
    if len(max_lis) > 0 and max_lis[-1] < arr[-1]:
        max_lis.append(arr[-1])
    
    return max_lis

def naive_lis(arr: list[int]) -> list[int]:
    max_lis = []
    for i in range(len(arr)):
        lis_i = naive_lis_recursive(arr[:i+1])
        if len(max_lis) < len(lis_i):
            max_lis = lis_i
    return max_lis


if __name__ == "__main__":
    a = random_list(30)
    print(a)

    start_time = time.time()
    lis = naive_lis(a)
    runtime_naive = time.time() - start_time
    print(f'{lis}\nLength: {len(lis)}\n{runtime_naive:.2f} sec\n')

    start_time = time.time()
    lis = memoized_lis(a)
    runtime_memoized = time.time() - start_time
    print(f'{lis}\nLength: {len(lis)}\n{runtime_memoized:.2f} sec')