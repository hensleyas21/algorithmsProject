import time
import random

# generates a list of length n filled with random integers [1, n]
def random_list(n: int) -> list[int]:
    return [random.randint(1, n) for _ in range(n)]

# the recursive step of the naive solution for finding longest increasing subsequence
# this method should not be called directly, use naive_lis(arr) instead
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

# finds the longest increasing subsequence using the naive solution
def naive_lis(arr: list[int]) -> list[int]:
    max_lis = []

    # calculates the LIS for arr[0:0], arr[0:1], arr[0:2], ... , arr[0:n] and set max_lis to the longest solution
    for i in range(len(arr)):
        lis_i = naive_lis_recursive(arr[:i+1])
        if len(max_lis) < len(lis_i):
            max_lis = lis_i
    return max_lis

# finds the longest increasing subsequence using the binary tree solution
def binary_search_lis(arr: list[int]) -> list[int]:
    if len(arr) == 0:
        return []
    
    lis = [arr[0]]
    for i in range(1, len(arr)):
        # if the next value of arr is greater than the last value in the LIS, add it to the LIS.
        # otherwise, use binary search to find where arr[i] goes in the LIS and substitute the existing value in the LIS with arr[i]
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
    a = random_list(50)
    print(f'Original List:\n{a}\nLength: {len(a)}')

    start_time = time.time()
    lis = naive_lis(a)
    runtime_naive = time.time() - start_time
    print(f'\nNaive Solution:\n{lis}\nLength: {len(lis)}\n{runtime_naive:.2f} sec')

    start_time = time.time()
    lis = binary_search_lis(a)
    runtime_naive = time.time() - start_time
    print(f'\nBinary Search Solution:\n{lis}\nLength: {len(lis)}\n{runtime_naive:.2f} sec')