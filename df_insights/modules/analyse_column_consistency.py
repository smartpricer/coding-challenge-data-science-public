def analyze_column_consistency(df):
    import pandas as pd
    """
    Analyzes the consistency of columns by checking for duplicates, missing values, format, length, and data types.

    Args:
        df (pd.DataFrame): The input dataframe.

    Returns:
        pd.DataFrame: A summary dataframe with column-wise consistency details.
    """
    # Initialize dictionary for faster processing
    report_dict = {
        'Data Type': df.dtypes,
        'Total Values': df.shape[0],
        'Unique Values': df.nunique(),
        'Duplicate Values': df.duplicated().sum(),
        'Missing Values': df.isnull().sum(),
        'Percentage Missing': df.isnull().mean() * 100,
    }

    # Compute max/min length only for string/object columns
    object_columns = df.select_dtypes(include=['object', 'string'])
    if not object_columns.empty:
        report_dict['Max Length'] = object_columns.applymap(lambda x: len(str(x)) if pd.notnull(x) else 0).max()
        report_dict['Min Length'] = object_columns.applymap(lambda x: len(str(x)) if pd.notnull(x) else 0).min()
    else:
        report_dict['Max Length'] = pd.Series([None] * len(df.columns), index=df.columns)
        report_dict['Min Length'] = pd.Series([None] * len(df.columns), index=df.columns)

    # Format consistency: Ratio of unique values to total rows (only for non-numeric columns)
    non_numeric_columns = df.select_dtypes(exclude=['number'])
    if not non_numeric_columns.empty:
        report_dict['Format Consistency'] = non_numeric_columns.nunique() / df.shape[0]
    else:
        report_dict['Format Consistency'] = pd.Series([None] * len(df.columns), index=df.columns)

    # Convert dictionary to DataFrame
    consistency_report = pd.DataFrame(report_dict)

    return consistency_report