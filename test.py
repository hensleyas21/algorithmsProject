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
    def zig_zag(n: int = 100) -> list[int]:
        sequence = []
        for i in range(1, n + 1):
            if i % 2 == 1:
                sequence.append(i + 1)
            else:
                sequence.append(i - 1)
        return sequence
    
    @staticmethod
    def random(n: int = 100) -> list[int]:
        return random.choices(range(1, n + 1), k=n)


def test():
    def run_test(generator, amount: list[int], verbose: bool = True):
        seqs = [generator(n=n) for n in amount]
        
        for seq in seqs:
            total_niave = 0
            total_efficient = 0
            print(f"Started {generator.__name__} for n={len(seq)}")

            for _ in range(10):
                start_time = time.time()
                main.naive_lis(seq)
                total_time = (time.time() - start_time) * 1000
                total_niave += total_time
                if verbose: print(f"Naive solution for n={len(seq)} on {generator.__name__}: {total_time:.5f} ms")        
                start_time = time.time()
                main.binary_search_lis(seq)
                total_time = (time.time() - start_time) * 1000
                total_efficient += total_time
                if verbose: print(f"Efficient solution for n={len(seq)} on {generator.__name__}: {total_time:.5f} ms")    
        
            print(f"Naive solution avg for n={len(seq)} on {generator.__name__}: {(total_niave / 10):.5f} ms")                    
            print(f"Efficient solution avg for n={len(seq)} on {generator.__name__}: {(total_efficient / 10):.5f} ms")        


    t1 = multiprocessing.Process(target=run_test(Sequences.strictly_increase, [5, 10, 15, 20, 25], verbose=False))
    t1.start()
    t2 = multiprocessing.Process(target=run_test(Sequences.strictly_decrease, [5, 10, 15, 20, 25], verbose=False))
    t2.start()
    t3 = multiprocessing.Process(target=run_test(Sequences.alternating_high_low, [5, 10, 15, 20, 25, 30], verbose=False))
    t3.start()
    t4 = multiprocessing.Process(target=run_test(Sequences.zig_zag, [5, 10, 15, 20, 25], verbose=False))
    t4.start()
    t5 = multiprocessing.Process(target=run_test(Sequences.random, [5, 10, 15, 20, 25], verbose=False))
    t5.start()  
    
if __name__ == '__main__':
    test()