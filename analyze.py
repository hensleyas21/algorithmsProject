import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def analyze_naive():
    # Step 1: Read the CSV file
    file_path = "test_results_naive.csv"  # Replace with your actual file path
    data = pd.read_csv(file_path)

    # Step 2: Prepare for plotting
    sequence_types = data["Sequence"].unique()  # Get all unique sequence types

    # Step 3: Plot and export each sequence type
    for sequence in sequence_types:
        # Filter data for the current sequence type
        seq_data = data[data["Sequence"] == sequence]
        
        # Calculate mean times for each n
        mean_times = seq_data.groupby("n")["Time (ms)"].mean().reset_index()
        unique_ns = np.sort(seq_data["n"].unique())
        mean_values = mean_times["Time (ms)"]
        
        # Generate smooth x values and 2^n trendline
        x_smooth = np.linspace(unique_ns.min(), unique_ns.max(), 500)  # 500 points for smoothness
        trendline_values = (2 ** x_smooth).astype(float)

        # Normalize trendline to match the mean scale
        scaling_factor = mean_values.iloc[-1] / (2 ** unique_ns[-1])
        trendline_values *= scaling_factor
        
        # Create the plot
        plt.figure(figsize=(10, 6))
        
        # Plot individual times
        plt.scatter(seq_data["n"], seq_data["Time (ms)"], color="blue", label="Individual Times", alpha=0.6)
        
        # Plot mean times
        plt.plot(mean_times["n"], mean_values, color="orange", label="Mean Times", marker="o")
        
        # Plot 2^n trendline
        plt.plot(x_smooth, trendline_values, color="green", linestyle="--", label="2^n Trendline")
        
        # Customize the plot
        plt.title(f"{sequence.replace('_', ' ').title()} Sequence, Naïve Algorithm Running Time")
        plt.xlabel("n")
        plt.ylabel("Time (ms)")
        plt.legend()
        plt.grid(True)
        
        # Save the plot as an image
        output_file = f"{sequence}_plot_naive.png"  # Replace with desired directory if needed
        plt.savefig(output_file)
        print(f"Saved plot for {sequence} as {output_file}")
        
        # Close the plot to free memory
        plt.close()

    print("All plots saved successfully.")

def analyze_efficient():
    file_path = "test_results_efficient.csv"  # Replace with your actual file path
    data = pd.read_csv(file_path)

    # Step 2: Prepare for plotting
    sequence_types = data["Sequence"].unique()  # Get all unique sequence types

    # Step 3: Plot and export each sequence type
    for sequence in sequence_types:
        # Filter data for the current sequence type
        seq_data = data[data["Sequence"] == sequence]
        
        # Calculate mean times for each n
        mean_times = seq_data.groupby("n")["Time (ms)"].mean().reset_index()
        
        # Generate smooth x values and n * log(n) trendline
        unique_ns = np.sort(seq_data["n"].unique())
        x_smooth = np.linspace(unique_ns.min(), unique_ns.max(), 500)  # 500 points for smoothness
        trendline_values = x_smooth * np.log(x_smooth)
        
        # Normalize trendline to match the mean scale
        scaling_factor = mean_times["Time (ms)"].iloc[-1] / trendline_values[-1]
        trendline_values *= scaling_factor
        
        # Create the plot
        plt.figure(figsize=(10, 6))
        
        # Plot individual times
        plt.scatter(seq_data["n"], seq_data["Time (ms)"], color="blue", label="Individual Times", alpha=0.6)
        
        # Plot mean times
        plt.plot(mean_times["n"], mean_times["Time (ms)"], color="orange", label="Mean Times", marker="o")
        
        # Plot n * log(n) trendline
        plt.plot(x_smooth, trendline_values, color="green", linestyle="--", label="n * log(n) Trendline")
        
        # Customize the plot
        plt.title(f"{sequence.replace('_', ' ').title()} Sequence, Efficient Algorithm Running Time")
        plt.xlabel("n")
        plt.ylabel("Time (ms)")
        plt.legend()
        plt.grid(True)
        
        # Save the plot as an image
        output_file = f"{sequence}_plot.png"  # Replace with desired directory if needed
        plt.savefig(output_file)
        print(f"Saved plot for {sequence} as {output_file}")
        
        # Close the plot to free memory
        plt.close()

    print("All plots saved successfully.")

analyze_efficient()
analyze_naive()