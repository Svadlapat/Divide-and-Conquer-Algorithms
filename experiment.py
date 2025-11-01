# experiment.py
import time
import tracemalloc
import random
import csv
from sorts import merge_sort, randomized_quick_sort  # quick_sort not needed here

# Experiment parameters
sizes = [1000, 5000, 10000, 20000]  # adjust based on your system
reps = 5  # number of repetitions per configuration

# Dataset generators
def gen_random(n):
    return [random.randint(0, n) for _ in range(n)]

def gen_sorted(n):
    return list(range(n))

def gen_rev_sorted(n):
    return list(range(n, 0, -1))

# Measure function that returns (time_sec, peak_memory_kb)
def measure_sort(func, arr, in_place=False):
    """
    Measures execution time and peak memory of the given sort function.
    """
    a_copy = arr[:]  # ensure independence between tests
    tracemalloc.start()
    start = time.perf_counter()
    
    if in_place:
        func(a_copy)
    else:
        _ = func(a_copy)
    
    elapsed = time.perf_counter() - start
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    return elapsed, peak / 1024.0  # peak memory in KB

# Main experiment loop
if __name__ == '__main__':
    random.seed(42)
    rows = []

    for n in sizes:
        for dtype, gen, in_place in [
            ('random', gen_random, False),
            ('sorted', gen_sorted, False),
            ('rev_sorted', gen_rev_sorted, False),
        ]:
            for rep in range(reps):
                arr = gen(n)

                # Merge Sort (not in-place)
                t_merge, m_merge = measure_sort(merge_sort, arr, in_place=False)

                # Randomized Quick Sort (in-place)
                arr_q = arr[:]
                t_q, m_q = measure_sort(randomized_quick_sort, arr_q, in_place=True)

                # Store results
                rows.append([n, dtype, 'merge_sort', t_merge, m_merge])
                rows.append([n, dtype, 'randomized_quick_sort', t_q, m_q])

                # Print progress
                print(f"n={n:6d} | type={dtype:11s} | rep={rep+1}/{reps} | "
                      f"merge={t_merge:.4f}s ({m_merge:.1f} KB) | "
                      f"quick={t_q:.4f}s ({m_q:.1f} KB)")

    # Write results to CSV
    with open('results.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['n', 'data_type', 'algorithm', 'time_sec', 'peak_mem_kb'])
        writer.writerows(rows)

    print("\n Experiment completed successfully! Results saved to 'results.csv'")
