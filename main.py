import os

from src.data_handler import load_sql_file_to_dataframe

# Data Report
from df_insights.modules.save_log_to_md import save_log_to_md

from preprocessing.preprocessing import prepare_data, plot_data

from modelling.model_pipeline import run_model_pipeline



df = load_sql_file_to_dataframe(os.path.join("data","tickets.db"))

consistency_report = save_log_to_md(df)

df = prepare_data(df)

plot_data(df, "dates", "valid_tickets")

print(df.head())

run_model_pipeline(df)