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

def binary_search_lis(arr: list[int]) -> list[int]:
    if len(arr) == 0:
        return []
    
    lis = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] > lis[-1]:
            lis.append(arr[i])
        else:
            low_idx = 0
            high_idx = len(lis) - 1
            while low_idx < high_idx:
                midpoint = (high_idx + low_idx) // 2
                if lis[midpoint] < arr[i]:
                    low_idx = midpoint + 1
                else:
                    high_idx = midpoint
            lis[low_idx] = arr[i]
    return lis


if __name__ == "__main__":
    a = random_list(100)
    print(f'Original List:\n{a}\nLength: {len(a)}')

    start_time = time.time()
    lis = naive_lis(a)
    runtime_naive = time.time() - start_time
    print(f'\nNaive Solution:\n{lis}\nLength: {len(lis)}\n{runtime_naive:.2f} sec')

    start_time = time.time()
    lis = binary_search_lis(a)
    runtime_naive = time.time() - start_time
    print(f'\nBinary Search Solution:\n{lis}\nLength: {len(lis)}\n{runtime_naive:.2f} sec')