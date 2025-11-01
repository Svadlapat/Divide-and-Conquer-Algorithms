# Divide-and-Conquer-Algorithms
Overview

This project explores two classic divide-and-conquer algorithms — Merge Sort and Quick Sort (Randomized) — through theoretical analysis and practical implementation.
It includes asymptotic analysis, recurrence relation solving, and empirical performance comparison based on time and memory usage.

Divide_and_conquer/
│
├─sorts.py #Contains Merge Sort, Quick Sort, and Randomized Quick Sort implementations
├─experiment.py   # Runs experiments on various dataset types and records performance
├─plot_results.py  # Plots and visualizes the recorded results
├─results.csv   # Output file storing performance data (generated after experiment)
└─README.md       # Project documentation


Merge Sort:

Approach: Divide array into halves, sort each recursively, and merge them.

Recurrence Relation:T(n)=2T(2n​)+O(n)
Using the Master Theorem,T(n)=Θ(nlogn)
Best / Average / Worst Case: O(n log n)

Randomized Quick Sort:

Approach: Partition array around a random pivot, recursively sort partitions.

Recurrence Relation:T(n)=T(k)+T(n−k−1)+O(n)
On average,T(n)=O(nlogn)
Worst-case (rare for randomized version): O(n²)

Experimental Setup:

The experiments compare both algorithms on datasets of sizes:
[1000, 5000, 10000, 20000]
Each dataset type:
Random
Sorted
Reverse Sorted

Each test is repeated 5 times to ensure consistency.
Performance metrics recorded:
Execution time (seconds)
Peak memory usage (KB)

Running the Code
Step 1 — Run the experiment:
``` bash
python experiment.py
```
This generates results.csv containing timing and memory data.

Step 2 — Plot and analyze results:
```bash
python plot_results.py
```

This creates graphs comparing Merge Sort and Randomized Quick Sort across all dataset types.

