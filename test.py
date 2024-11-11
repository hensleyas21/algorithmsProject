import main
import time
import random
import multiprocessing
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
    # strictly increase test

    def run_test(generator):
        seqs = [generator(n=n) for n in [10, 50]]
        for seq in seqs:
            start_time = time.time()
            main.naive_lis(seq)
            total_time = time.time() - start_time
            print(f"Naive solution for n={len(seq)} on {generator.__name__}: {total_time:.2f} sec")        
            start_time = time.time()
            main.binary_search_lis(seq)
            total_time = time.time() - start_time
            print(f"Efficient solution for n={len(seq)} on {generator.__name__}: {total_time:.2f} sec")    
            
    t1 = multiprocessing.Process(target=run_test(Sequences.strictly_increase))
    t1.start()
    t2 = multiprocessing.Process(target=run_test(Sequences.strictly_decrease))
    t2.start()
    t3 = multiprocessing.Process(target=run_test(Sequences.alternating_high_low))
    t3.start()
    t4 = multiprocessing.Process(target=run_test(Sequences.constant))
    t4.start()
    t5 = multiprocessing.Process(target=run_test(Sequences.zig_zag))
    t5.start()
    t6 = multiprocessing.Process(target=run_test(Sequences.repeated_pattern))
    t6.start()
    t7 = multiprocessing.Process(target=run_test(Sequences.random))
    t7.start()

    