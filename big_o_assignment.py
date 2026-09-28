"""
Big O Classification and Pair-Counting Benchmark
"""

# Part 1 - Classify These Functions

# Function A: O(1)
# Reason: Accessing data[0] takes constant time regardless of the size of the list.

# Function B: O(n)
# Reason: The function loops through every item in data exactly once.

# Function C: O(n^2)
# Reason: Two nested loops each run n times, producing n * n iterations.

# Function D: O(log n)
# Reason: The value of n is divided by 2 each loop, so the number of iterations grows logarithmically.

# Function E: O(n log n)
# Reason: sum(data) is O(n), sorted(data) is O(n log n), and data[0] is O(1), so sorting dominates overall.


import random
import time


def count_pairs_quadratic(data, target):
    """Count index pairs whose values sum to target using nested loops: O(n^2)."""
    count = 0

    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] + data[j] == target:
                count += 1

    return count


def count_pairs_linear(data, target):
    """Count index pairs whose values sum to target using a dictionary: O(n) average time."""
    seen = {}
    count = 0

    for number in data:
        complement = target - number
        count += seen.get(complement, 0)
        seen[number] = seen.get(number, 0) + 1

    return count


def benchmark():
    random.seed(42)
    sizes = [1000, 5000, 10000]
    target = 100

    for size in sizes:
        data = [random.randint(0, 100) for _ in range(size)]

        start = time.perf_counter()
        quadratic_count = count_pairs_quadratic(data, target)
        quadratic_time = time.perf_counter() - start

        start = time.perf_counter()
        linear_count = count_pairs_linear(data, target)
        linear_time = time.perf_counter() - start

        # Both functions should return the same number of pairs.
        assert quadratic_count == linear_count

        print(
            f"n={size:,}: "
            f"O(n^2) = {quadratic_time:.6f}s | "
            f"O(n) = {linear_time:.6f}s | "
            f"pairs = {quadratic_count}"
        )


if __name__ == "__main__":
    benchmark()


# Benchmark output from one run:
# n=1,000: O(n^2) = 0.030754s | O(n) = 0.000141s | pairs = 4893
# n=5,000: O(n^2) = 0.851793s | O(n) = 0.000742s | pairs = 123959
# n=10,000: O(n^2) = 3.542534s | O(n) = 0.001301s | pairs = 495398
