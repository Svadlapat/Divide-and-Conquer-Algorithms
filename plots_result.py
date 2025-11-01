# plot_results.py
import pandas as pd
import matplotlib.pyplot as plt

# Load results file generated from experiment.py
df = pd.read_csv('results.csv')
# Ensure proper sorting by 'n' (input size)
df = df.sort_values(by='n')
# Plot average runtime for each data type
for dtype in df['data_type'].unique():
    fig, ax = plt.subplots(figsize=(8, 5))
    # Filter data for this input type (random, sorted, etc.)
    subset = df[df['data_type'] == dtype]
    # Plot each algorithm separately
    for alg in subset['algorithm'].unique():
        grouped = subset[subset['algorithm'] == alg].groupby('n')['time_sec'].mean()
        ax.plot(grouped.index, grouped.values, marker='o', label=alg)
    
    ax.set_title(f'Average Runtime on {dtype.capitalize()} Data')
    ax.set_xlabel('Input Size (n)')
    ax.set_ylabel('Average Time (seconds)')
    ax.legend()
    ax.grid(True)
    
    # Save each plot as an image
    plt.tight_layout()
    plt.savefig(f'runtime_{dtype}.png')
    plt.show()

# (Optional) Plot peak memory usage comparison
for dtype in df['data_type'].unique():
    fig, ax = plt.subplots(figsize=(8, 5))
    subset = df[df['data_type'] == dtype]
    for alg in subset['algorithm'].unique():
        grouped = subset[subset['algorithm'] == alg].groupby('n')['peak_mem_kb'].mean()
        ax.plot(grouped.index, grouped.values, marker='s', label=alg)
    
    ax.set_title(f'Average Peak Memory Usage on {dtype.capitalize()} Data')
    ax.set_xlabel('Input Size (n)')
    ax.set_ylabel('Peak Memory (KB)')
    ax.legend()
    ax.grid(True)
    
    plt.tight_layout()
    plt.savefig(f'memory_{dtype}.png')
    plt.show()
