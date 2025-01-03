import time

# the recursive step of the naive solution for finding
# the LIS in arr[0:idx] that includes the element at idx
#
# this method should not be called directly, use naive_lis(arr) instead
def naive_lis_ending_at_idx(arr: list[int], idx: int) -> list[int]:
    if idx == 0:
        return [arr[0]]
        
    max_lis = [arr[idx]]

    for x in range(idx):
        if arr[x] < arr[idx]:
            lis_i = naive_lis_ending_at_idx(arr, x)
            if len(max_lis) < len(lis_i) + 1:
                max_lis = lis_i
    
    if max_lis[-1] < arr[idx]:
        max_lis.append(arr[idx])
    
    return max_lis

# finds the longest increasing subsequence using the naive solution
def naive_lis(arr: list[int]) -> list[int]:
    max_lis = []

    # calculates the LIS for arr[0:0], arr[0:1], arr[0:2], ... , arr[0:n] and set max_lis to the longest solution
    for i in range(len(arr)):
        lis_i = naive_lis_ending_at_idx(arr, i)
        if len(max_lis) < len(lis_i):
            max_lis = lis_i
    return max_lis

# finds the longest increasing subsequence using the binary tree solution
def binary_search_lis(arr: list[int]) -> list[int]:
    pred = [None] * len(arr)
    min_end_index = [-1] * (len(arr)+1)

    lis_len = 0
    
    for i in range(len(arr)):
        # if arr[i] is greater than all elements in the current LIS, add it to the end
        # otherwise, use binary search to find the position where arr[i] can replace or extend the LIS
        if lis_len == 0 or arr[i] > arr[min_end_index[lis_len]]:
            new_lis_len = lis_len + 1
        else:
            low = 1
            high = lis_len + 1
            while low < high:
                mid = low + (high-low)//2
                if arr[min_end_index[mid]] >= arr[i]:
                    high = mid
                else:
                    low = mid + 1
            new_lis_len = low

        # store the index of the predecessor for arr[i], which is the last element in subsequence of length new_lis_len-1
        pred[i] = min_end_index[new_lis_len-1]

        # update min_end_index for the subsequence of length new_lis_len with the current element's index
        min_end_index[new_lis_len] = i

        # if a longer subsequence is found, update lis_len
        if new_lis_len > lis_len:
            lis_len = new_lis_len

    # reconstuct the LIS beginning with the last element in min_end_index
    # use pred to find the element that belongs before until the LIS is complete
    s = [None] * lis_len
    k = min_end_index[lis_len]
    for i in range(lis_len-1, -1, -1):
        s[i] = arr[k]
        k = pred[k]
    
    return s
    

if __name__ == "__main__":
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