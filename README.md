# Data Science Coding Challenge

Data Science Coding Challenge - time series forecasting

# The Challenge
Welcome to the  Ski Ticket Forecasting Challenge! 
In this repository [ https://github.com/smartpricer/coding-challenge-data-science-public ] you will find a SQLite file containing a table named "timeseries". This table includes the daily number of valid ski tickets sold for the winter seasons 2016/2017 to 2021/2022.
Your main objective is to forecast ticket sales for the next season 2022/2023, covering the period from December 10, 2022, to April 15, 2023 (10.12.2022 - 15.04.2023).

To assist you, we’ve included some basic code to help you extract data from the SQLite file. :laufende_sanduhr: Time Limit: 1–2 hours :hammer_und_schraubenschlüssel: Tools: You are free to use any tools of your choice (but please don't spend more than 2 hours on that challenge.)

We know that this challenge is quite open-ended, and one could spend days or even weeks refining the model. To keep things focused, we’ve outlined three key tasks:

1. Get an understanding of the data at hand.
    - a) What do you see (patterns/potential issues)?

2. Choose the algorithm / library for the forecasting tool. (Prophet, ARIMA-Family, Gradient-boosted-Trees etc)
    - b) Which forecasting model did you choose and why?

3. Implement a basic model as an initial MVP (minimum viable product) that predicts the next season and export your results as a CSV file.
    - c) Are there steps you were unable to finish?

    - d) Suggest 3 additional steps/features to add.


### ! Bonus Tasks (Optional) 4) Visualize your results: Create graphs to support your findings. 5) Validate your predictions: Implement a validation method. 6) Dockerize your application: Make it easily deployable.

- Deliverable / Expectation
We expect two key deliverables:
- A GitHub repository that contains your prediction tool (Fork this one as starting point)
- A README.md with Documentation. Use this README with the instruction and add your answers to the questions (a-e), as well as your explanation and thoughts.

Once again, we understand that 1 to 2 hours is not a great amount of time, so if you don’t complete everything, use the README to document critical decisions, assumptions, and next steps.

- e)How did you use AI to help you in the process?

- Get Started: Clone this repository [ https://github.com/smartpricer/coding-challenge-data-science-public ], Load the SQLite database, Explore the data, Implement your forecasting model, Document your findings by adding a README file & !!! Commit regularly & at the latest after 2 hours.

We’re excited to see your approach—happy forecasting! :ski::balkendiagramm:


1) Understanding of the Data (Patters and potential Issues)

## Data Analysis Log

**Total Rows:** 683  
**Total Columns:** 2
**Total NaN Values:** 0
**Total Duplicated Rows:** 0
## Highly Unique Identifiers Consistency Report
| Column Name          | Data Type  | Unique Values | Duplicates | Missing Values | % Missing | Max Length | Min Length |
| ------------------ | ---------- | ------------ | ---------- | -------------- | --------- | ---------- | ---------- |
| dates                | datetime64[ns] | 683          | 0          | 0              | 0.00      | N/A        | N/A        |
## Composite Key Found
- `dates, valid_tickets`


## Full Dataset Consistency Report
| Column Name          | Data Type      | Unique Values | Duplicates | Missing Values | % Missing | Max Length | Min Length |
| ------------------   | ----------     | ------------  | ---------- | -------------- | --------- | ---------- | ---------- |
| dates                | datetime64[ns] | 683           | 0          | 0              | 0.00      | N/A        | N/A        |
| valid_tickets        | object         | 565           | 0          | 0              | 0.00      | 5.0        | 1.0        |

# Data Preparation

Changed column names: "Ski Day": "dates", "valid_tickets": "valid_tickets"
Changed columns dtypes: 
    df["dates"] = pd.to_datetime(df["dates"])
    df["valid_tickets"]  = df["valid_tickets"].astype(int)

Added features from Datetime col 
feats = ["year", "month", "day", "dayofweek", "is_weekend"]


# Plot the data and EDA

### Distribution Plot in Plots/Ski_Ticket_Sales_Over_Time.png

From Aggregations and Plots i can come to the following conlusions:

### Valid Tickets sold per Year
df.groupby(["year"])["valid_tickets"].sum()

2016       163.076
2017     1.400.349
2018     1.462.129
2019     1.487.118
2020     1.003.606
2021       168.056
2022        16.041

# Entries per Year
df["dates"].dt.year.value_counts()

2019    143
2017    139
2018    134
2020    129
2021     81
2022     32
2016     25

Big Growth then Big Drop

- 2016 is much lower than all subsequent years, suggesting it might have been a partial year of operation or incomplete data collection.
- 2017–2019 increase steadily, reaching a peak in 2019 (1.49 million tickets).
- 2020 drops to about 1.0 million—likely due to pandemic impacts or other disruptions.
- 2021 and 2022 plummet even further (168 k and 16 k), which could be an actual collapse in sales (e.g. pandemic shutdown, limited season) or might indicate incomplete data.

Number of Entries (Data Points) Varies

- 2019 has 143 entries, whereas 2016 only has 25. That discrepancy could mean:
    - Partial coverage (maybe you only started tracking in mid‐2016).
    - Shorter or longer operating seasons in some years (e.g., 2021/2022 reduced season).
    - Inconsistent data‐collection methods across years.

Possible Data Gaps or Missing Periods

- The huge drop in sales around 2021–2022, coupled with the fewer entries, suggests big data holes or actual closures. If the resort was closed, those could be valid zeros; otherwise, they may just be missing data.

Things to Watch For

- Context of 2016 – Was it a partial year, a trial period, or incomplete logs?
- Pandemic Effects – 2020 onward is likely affected by external shutdowns/restrictions.
- Reporting Consistency – The varying number of entries per year might mean your data is patchy. That will matter for forecasts and analyses


2. Choose the algorithm / library for the forecasting tool. 

### Timeseries (Model_Pipeline)

- Algorhythms:
    - Random Forest Regressor: Easy to use, robust, handles non-linearity well, and requires minimal tuning.
    - XGBoost: Faster, more efficient, handles large datasets well, and provides better accuracy with hyperparameter tuning.

    - Usability: Both models are widely used, easy to implement, and require minimal preprocessing.
    - Lightness: Random Forest is lightweight but slower; XGBoost is optimized for speed and efficiency.

3. Implement a basic model as an initial MVP

### FE
    Transforms a date column into
        - year
        - month
        - day
        - dayofweek
        - is_weekend
    
### Training and Forecasting
    Splits the dataset into training (before 2022) and testing (2022).

    Defines input features (month, day, dayofweek, is_weekend) and target variable (valid_tickets).

    Trains the given model and evaluates its performance using Root Mean Squared Error (RMSE).

    Generates future ticket sales predictions for December 2022 - April 2023.

    Saves trained models to the models/ directory using joblib.

    Plots and saves forecast results in plots/.

### Model Training and Execution

    Two models are trained and compared:

    Random Forest (RandomForestRegressor)

    XGBoost (XGBRegressor)

    Forecast results are saved in CSV format inside the forecasts/ directory.



4) Visualization and MVP Export

### Outputs

    Trained Models (models/RandomForest.pkl, models/XGBoost.pkl)

    Forecast Plots (plots/forecast_RandomForest.png, plots/forecast_XGBoost.png)

    Predicted Data (forecasts/ski_ticket_forecast_rf.csv, forecasts/ski_ticket_forecast_xgb.csv)

### Results:

RandomForest RMSE: 8022.97
XGBoost RMSE: 7716.61


### Additional Steps or Added Features:

    - Incorporate External Data – Enhance model accuracy by integrating weather data (snowfall, temperature) and holiday/special event indicators to capture demand fluctuations.

    - Hyperparameter Optimization – Use GridSearchCV or Optuna to fine-tune model parameters, improving prediction accuracy and reducing overfitting.

    - Deploy And dockerize the models – 

### How did i use AI

    - Code Refactorization
    - Debugging
    - Help with the documentation


