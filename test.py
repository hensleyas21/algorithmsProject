import main
import time
import random

# messing around with stuff
class Sequences:
    @staticmethod
    def strickly_increase(n: int = 100) -> list[int]:
        return list(range(1, n + 1))

    @staticmethod
    def strickly_decrease(n: int = 100) -> list[int]:
        return list(range(n + 1, 1, -1))
    
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
        return [constant for _ in random(1, n + 1)]
    
    @staticmethod
    def zig_zag(n: int = 100) -> list[int]:
        sequence = []
        for i in range(1, n):
            if i % 2 == 1:
                sequence.append(i + 1)
            else:
                sequence.append(i - 1)
        return sequence
    
    @staticmethod
    # TODO: fix
    def repeated_pattern(n: int = 100) -> list[int]:
        if n % 2 == 1:
            pattern = [random.random() for _ in range(3)]
            return [num for num in pattern for _ in range(0, n, 3)]
        else:
            pattern = [random.random() for _ in range(2)]
            return [num for num in pattern for _ in range(0, n, 2)]

    @staticmethod
    def random_sequence(n: int = 100) -> list[int]:
        return main.random_list(n)


if __name__ == '__main__':
    a = main.random_list(10000000)
    start_time = time.time()
    lis = main.binary_search_lis(a)
    runtime_naive = time.time() - start_time
    print(f'Binary Search Solution:\n{lis}\nLength: {len(lis)}\n{runtime_naive:.2f} sec')