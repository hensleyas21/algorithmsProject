import main
import time
import random

import random

# messing around with stuff
class Sequences:
    @staticmethod
    def strictly_increase(n: int = 100) -> list[int]:
        return list(range(1, n + 1))

    @staticmethod
    def strictly_decrease(n: int = 100) -> list[int]:
        return list(range(n, 0, -1))
    
    @staticmethod
    def alternating_high_low(n: int = 100) -> list[int]:
        sequence = []
        high_idx = 0
        for i in range(1, n + 1):
            if i % 2 == 1:
                sequence.append(n - high_idx)
                high_idx += 1 
            else:
                sequence.append(i)
        return sequence

    @staticmethod
    def constant(n: int = 100) -> list[int]:
        constant = random.random()
        return [constant for _ in range(1, n + 1)]
    
    @staticmethod
    def zig_zag(n: int = 100) -> list[int]:
        sequence = []
        for i in range(1, n + 1):
            if i % 2 == 1:
                sequence.append(i + 1)
            else:
                sequence.append(i - 1)
        return sequence
    
    @staticmethod
    def repeated_pattern(n: int = 100) -> list[int]:
        if n % 2 == 1:
            pattern = [random.randint(1, 10) for _ in range(3)]
            return (pattern * ((n // 3) + 1))[:n]
        else:
            pattern = [random.randint(1, 10) for _ in range(2)]
            return (pattern * ((n // 2) + 1))[:n]

    @staticmethod
    def random(n: int = 100) -> list[int]:
        return random.choices(range(1, n + 1), k=n)



if __name__ == '__main__':
    a = main.random_list(10000000)
    start_time = time.time()
    lis = main.binary_search_lis(a)
    runtime_naive = time.time() - start_time
    print(f'Binary Search Solution:\n{lis}\nLength: {len(lis)}\n{runtime_naive:.2f} sec')