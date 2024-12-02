import time
# from test import Sequences

# the recursive step of the naive solution for finding
# the LIS that includes the final element in the inputted list
#
# this method should not be called directly, use naive_lis(arr) instead
def naive_lis_recursive(subarr: list[int]) -> list[int]:
    if len(subarr) <= 1:
        return subarr
    
    max_lis = [subarr[-1]]

    for i in range(len(subarr)):
        if subarr[i] < subarr[-1]:
            lis_i = naive_lis_recursive(subarr[:i+1])
            if len(max_lis) < len(lis_i) + 1:
                max_lis = lis_i
    
    if len(max_lis) > 0 and max_lis[-1] < subarr[-1]:
        max_lis.append(subarr[-1])
    
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
    indices = [0]
    pred = [-1] * len(arr)

    for i in range(1, len(arr)):
        if arr[i] > lis[-1]:
            pred[i] = indices[-1]
            lis.append(arr[i])
            indices.append(i)
        else:
            low = 0
            high = len(lis) - 1
            while low < high:
                mid = (high + low) // 2
                if lis[mid] < arr[i]:
                    low = mid + 1
                else:
                    high = mid
            lis[low] = arr[i]
            indices[low] = i
            if low > 0:
                pred[i] = indices[low-1]
    
    max_lis = []
    k = indices[-1]
    while k >= 0:
        max_lis.append(arr[k])
        k = pred[k]
    max_lis.reverse()
    return max_lis


if __name__ == "__main__":
    # a = Sequences.random(50)
    a = [34, 1, 56, 47, 13, 52, 25, 12, 70, 39, 9, 66, 37, 48, 63, 45, 50, 8, 67, 5, 
 17, 31, 3, 29, 41, 18, 53, 72, 33, 38, 69, 7, 71, 30, 21, 73, 40, 19, 24, 15, 
 28, 55, 44, 35, 46, 4, 36, 61, 68, 26, 62, 20, 60, 51, 10, 11, 49, 59, 32, 74, 
 14, 22, 16, 64, 65, 23, 58, 2, 27, 75, 42, 43, 57, 74, 76, 48, 13, 71, 66, 49]

    print(f'Original List:\n{a}\nLength: {len(a)}')
    start_time = time.time()
    lis = naive_lis(a)
    runtime_naive = time.time() - start_time
    print(f'\nNaive Solution:\n{lis}\nLength: {len(lis)}\n{runtime_naive:.2f} sec')
    start_time = time.time()
    lis = binary_search_lis(a)
    runtime_naive = time.time() - start_time
    print(f'\nBinary Search Solution:\n{lis}\nLength: {len(lis)}\n{runtime_naive:.2f} sec')