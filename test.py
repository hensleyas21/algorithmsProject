import main
import time
import random
import multiprocessing
import csv


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


def run_test(generator, amounts, queue):
    results = []
    for n in amounts:
        seq = generator(n=n)
        for _ in range(10):
            start_time = time.time()
            main.naive_lis(seq)
            naive_time = (time.time() - start_time) * 1000
            results.append((generator.__name__, n, "Naive", naive_time))

            start_time = time.time()
            main.binary_search_lis(seq)
            efficient_time = (time.time() - start_time) * 1000
            results.append((generator.__name__, n, "Efficient", efficient_time))
    queue.put(results)


def test():
    sequence_generators = [
        Sequences.strictly_increase,
        Sequences.strictly_decrease,
        Sequences.alternating_high_low,
        Sequences.zig_zag,
        Sequences.random,
    ]
    n_values = [5, 10, 15, 20, 25]
    queue = multiprocessing.Queue()
    processes = []

    for generator in sequence_generators:
        process = multiprocessing.Process(target=run_test, args=(generator, n_values, queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    # Collect results from all processes
    results = []
    while not queue.empty():
        results.extend(queue.get())

    # Write results to a CSV file
    with open("test_results.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Sequence", "n", "Algorithm", "Time (ms)"])
        writer.writerows(results)


if __name__ == "__main__":
    test()