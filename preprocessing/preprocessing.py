import pandas as pd
import matplotlib.pyplot as plt

def get_datetime_features(df: pd.DataFrame, date_col: str) -> pd.DataFrame:
    """ Gets features out of datetime"""
    df["year"] = df[date_col].dt.year
    df["month"] = df[date_col].dt.month
    df["day"] = df[date_col].dt.day
    df["dayofweek"] = df[date_col].dt.dayofweek
    df["is_weekend"] = (df["dayofweek"] >= 5).astype(int)
    return df

def plot_data(df: pd.DataFrame, date_col: str, target: str):
    """Plots the time series data."""
    plt.figure(figsize=(12,6))
    plt.plot(df[date_col], df[target], label='Valid Tickets Sold', color='blue')
    plt.xlabel('Date')
    plt.ylabel('Tickets Sold')
    plt.title('Ski Ticket Sales Over Time')
    plt.legend()
    name = 'Ski_Ticket_Sales_Over_Time'
    plt.savefig(f"plots/{name}", dpi=300, bbox_inches='tight')
    plt.show()

def prepare_data(df: pd.DataFrame)  -> pd.DataFrame:
    """ 
    Prepare the Data for Forcasting
    Change column Names
    """
    df = df.rename(columns={"Ski Day": "dates", "valid_tickets": "valid_tickets"})
    df["dates"] = pd.to_datetime(df["dates"])
    df["valid_tickets"]  = df["valid_tickets"].astype(int)
    df = df.sort_values(by="dates")
    df = get_datetime_features(df, "dates")

    return df




