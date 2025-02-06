import xgboost as xgb
from sklearn.ensemble import RandomForestRegressor

from.model_comparison import train_and_forecast

def run_model_pipeline(df):

    rf_model = RandomForestRegressor(n_estimators=500, random_state=42)
    xgb_model = xgb.XGBRegressor(n_estimators=500, learning_rate=0.05, random_state=42)

    rf_forecast = train_and_forecast(rf_model, "RandomForest", df)
    xgb_forecast = train_and_forecast(xgb_model, "XGBoost", df)

    # Save forecasts
    rf_forecast.to_csv("forecasts/ski_ticket_forecast_rf.csv", index=False)
    xgb_forecast.to_csv("forecasts/ski_ticket_forecast_xgb.csv", index=False)
    print("Forecasts saved to CSV.")