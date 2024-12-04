import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def analyze_naive():
    file_path = "test_results_naive.csv" 
    data = pd.read_csv(file_path)

    sequence_types = data["Sequence"].unique()  

    for sequence in sequence_types:
        seq_data = data[data["Sequence"] == sequence]
        mean_times = seq_data.groupby("n")["Time (ms)"].mean().reset_index()
        unique_ns = np.sort(seq_data["n"].unique())
        mean_values = mean_times["Time (ms)"]
        x_smooth = np.linspace(unique_ns.min(), unique_ns.max(), 500)
        trendline_values = (2 ** x_smooth).astype(float)
        scaling_factor = mean_values.iloc[-1] / (2 ** unique_ns[-1])
        trendline_values *= scaling_factor
        plt.figure(figsize=(10, 6))
        plt.scatter(seq_data["n"], seq_data["Time (ms)"], color="blue", label="Individual Times", alpha=0.6)
        plt.plot(mean_times["n"], mean_values, color="orange", label="Mean Times", marker="o")
        plt.plot(x_smooth, trendline_values, color="green", linestyle="--", label="2^n Trendline")
        plt.title(f"{sequence.replace('_', ' ').title()} Sequence, Naïve Algorithm Running Time")
        plt.xlabel("n")
        plt.ylabel("Time (ms)")
        plt.legend()
        plt.grid(True)
        
        output_file = f"{sequence}_plot_naive.png"  # Replace with desired directory if needed
        plt.savefig(output_file)
        print(f"Saved plot for {sequence} as {output_file}")
        
        plt.close()

    print("All plots saved successfully.")

def analyze_efficient():
    file_path = "test_results_efficient.csv"  
    data = pd.read_csv(file_path)

    sequence_types = data["Sequence"].unique()  

    for sequence in sequence_types:
        seq_data = data[data["Sequence"] == sequence]
        mean_times = seq_data.groupby("n")["Time (ms)"].mean().reset_index()
        unique_ns = np.sort(seq_data["n"].unique())
        x_smooth = np.linspace(unique_ns.min(), unique_ns.max(), 500) 
        trendline_values = x_smooth * np.log(x_smooth)
        scaling_factor = mean_times["Time (ms)"].iloc[-1] / trendline_values[-1]
        trendline_values *= scaling_factor
        plt.figure(figsize=(10, 6))
        plt.scatter(seq_data["n"], seq_data["Time (ms)"], color="blue", label="Individual Times", alpha=0.6)
        plt.plot(mean_times["n"], mean_times["Time (ms)"], color="orange", label="Mean Times", marker="o")
        plt.plot(x_smooth, trendline_values, color="green", linestyle="--", label="n * log(n) Trendline")
        plt.title(f"{sequence.replace('_', ' ').title()} Sequence, Efficient Algorithm Running Time")
        plt.xlabel("n")
        plt.ylabel("Time (ms)")
        plt.legend()
        plt.grid(True)
        
        output_file = f"{sequence}_plot.png"
        plt.savefig(output_file)
        print(f"Saved plot for {sequence} as {output_file}")

        plt.close()

    print("All plots saved successfully.")

analyze_efficient()
analyze_naive()