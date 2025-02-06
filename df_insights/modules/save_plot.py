import matplotlib.pyplot as plt
import os

def save_plot(plot_name, folder_name="plots"):
    
    """
    Saves the current Matplotlib figure to a specified folder (default: "plots").

    Parameters:
    - plot_name (str): The filename (without path) to save the plot as (e.g., "myplot.png").
    - folder_name (str): The directory in which to save the plot. Default is "plots".
    """
    # 1. Check if folder exists, if not, create it
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    # 2. Construct the full path to save the plot
    full_path = os.path.join(folder_name, plot_name)
    
    # 3. Save the current figure
    plt.savefig(full_path, dpi=300, bbox_inches='tight')  # bbox_inches='tight' helps with trimming whitespace
    
    print(f"Plot saved to: {full_path}")