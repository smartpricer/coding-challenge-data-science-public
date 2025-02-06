import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib

def get_datetime_features(df, date_col):
    """Extract datetime features from a date column."""
    df["year"] = df[date_col].dt.year
    df["month"] = df[date_col].dt.month
    df["day"] = df[date_col].dt.day
    df["dayofweek"] = df[date_col].dt.dayofweek
    df["is_weekend"] = (df["dayofweek"] >= 5).astype(int)
    return df

def prepare_data_pred(df: pd.DataFrame) -> pd.DataFrame:
    """Prepare the Data for Forecasting."""
    df = df.rename(columns={"Ski Day": "dates", "valid_tickets": "valid_tickets"})
    df["dates"] = pd.to_datetime(df["dates"])
    df = df.sort_values(by="dates")
    df = get_datetime_features(df, "dates")
    return df

def train_and_forecast(model, model_name, df):
    """Train model and forecast future sales."""
    train = df[df["year"] < 2022]
    test = df[df["year"] == 2022]
    
    features = ["month", "day", "dayofweek", "is_weekend"]
    target = "valid_tickets"
    
    X_train, X_test = train[features], test[features]
    y_train, y_test = train[target], test[target]
    
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    print(f"{model_name} RMSE: {rmse:.2f}")
    
    future_dates = pd.date_range("2022-12-10", "2023-04-15", freq="D")
    future_df = pd.DataFrame({"dates": future_dates})
    future_df = prepare_data_pred(future_df)
    future_X = future_df[features]
    
    future_df["predicted_tickets"] = model.predict(future_X)
    
    os.makedirs("models", exist_ok=True)
    os.makedirs("plots", exist_ok=True)
    
    model_path = os.path.join("models", f"{model_name}.pkl")
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")
    
    forecast_path = os.path.join("plots", f"forecast_{model_name}.png")
    plt.figure(figsize=(12, 6))
    plt.plot(df["dates"], df["valid_tickets"], label="Historical Sales", color="blue")
    plt.plot(future_df["dates"], future_df["predicted_tickets"], label=f"Forecast ({model_name})", color="red", linestyle="dashed")
    plt.xlabel("Date")
    plt.ylabel("Tickets Sold")
    plt.title(f"Ski Ticket Sales Forecast ({model_name})")
    plt.legend()
    plt.savefig(forecast_path)
    print(f"Plot saved to {forecast_path}")
    plt.show()
    
    return future_df

