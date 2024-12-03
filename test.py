import main
import time
import random
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


def run_test(generator, amounts, verbose: bool = False, naive: bool = True, efficient: bool = True):
    results = []
    for n in amounts:
        seq = generator(n=n)
        if verbose and naive: print(f"running n={n} for {generator.__name__} on naive")
        if verbose and efficient: print(f"running n={n} for {generator.__name__} on efficient")

        for _ in range(10):
            if naive:
                start_time = time.time()
                main.naive_lis(seq)
                naive_time = (time.time() - start_time) * 1000
                results.append((generator.__name__, n, "Naive", naive_time))


            if efficient:
                start_time = time.time()
                main.binary_search_lis(seq)
                efficient_time = (time.time() - start_time) * 1000
                results.append((generator.__name__, n, "Efficient", efficient_time))
    return results


def test():
    sequence_generators = [
        Sequences.strictly_increase,
        Sequences.strictly_decrease,
        Sequences.alternating_high_low,
        Sequences.zig_zag,
        Sequences.random,
    ]
    n_values = [5, 10, 15, 20, 25]

    # Collect results sequentially
    results = []
    for generator in sequence_generators:
        results.extend(run_test(generator, n_values, verbose=True, efficient=False))

    # Write results to a CSV file
    with open("test_results_naive.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Sequence", "n", "Algorithm", "Time (ms)"])
        writer.writerows(results)

    results = []
    results.extend(run_test(Sequences.strictly_increase, n_values + [10 ** 2, 10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7], verbose=True, naive=False))
    results.extend(run_test(Sequences.strictly_decrease, n_values + [10 ** 2, 10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7], verbose=True, naive=False))
    results.extend(run_test(Sequences.alternating_high_low, n_values + [10 ** 2, 10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7], verbose=True, naive=False))
    results.extend(run_test(Sequences.zig_zag, n_values + [10 ** 2, 10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7], verbose=True, naive=False))
    results.extend(run_test(Sequences.random, n_values + [10 ** 2, 10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7], verbose=True, naive=False))

  # Write results to a CSV file
    with open("test_results_efficient.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Sequence", "n", "Algorithm", "Time (ms)"])
        writer.writerows(results)


if __name__ == "__main__":
    test()
    