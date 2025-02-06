import os

from src.data_handler import load_sql_file_to_dataframe

# Data Report
from df_insights.modules.save_log_to_md import save_log_to_md

from preprocessing.preprocessing import prepare_data, plot_data

from modelling.model_pipeline import run_model_pipeline



DATA_PATH = os.path.join("data", "tickets.db")

def main():
    """Main script to run the ski ticket sales forecasting pipeline."""
    
    # Load data from SQLite database
    df = load_sql_file_to_dataframe(DATA_PATH)
    print("✅ Data successfully loaded!")

    # Generate data consistency report
    consistency_report = save_log_to_md(df)
    print("✅ Data consistency report generated!")

    # Preprocess data
    df = prepare_data(df)
    print("✅ Data preprocessing completed!")

    # Plot data visualization
    plot_data(df, "dates", "valid_tickets")
    print("✅ Data visualization saved!")

    # Display first few rows for validation
    print(df.head())

    # Run model pipeline (training & forecasting)
    run_model_pipeline(df)
    print("✅ Model pipeline executed successfully!")

if __name__ == "__main__":
    main()