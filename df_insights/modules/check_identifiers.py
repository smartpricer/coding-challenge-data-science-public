from .analyse_column_consistency import analyze_column_consistency
from .find_composite_keys import find_composite_keys

def check_identifiers(df):
    """
    Identifies potential unique identifiers by checking for high uniqueness
    and analyzes their consistency.

    Args:
        df (pd.DataFrame): The input dataframe.

    Returns:
        pd.DataFrame: A consistency report for highly unique columns.
    """
    # Check for unique values in each column
    unique_counts = df.nunique()

    # Define threshold for highly unique values (at least 95% unique)
    threshold = 0.95 * df.shape[0]
    highly_unique_columns = unique_counts[unique_counts > threshold]

    # Extract the column names that meet the uniqueness threshold
    highly_unique_identifiers = highly_unique_columns.index.tolist()

    # If no highly unique identifiers are found, return a message
    if not highly_unique_identifiers:
        print("No highly unique identifiers found.")
        return None

    # Generate a consistency report for the identified columns
    consistency_report = analyze_column_consistency(df[highly_unique_identifiers])

    composite_keys = find_composite_keys(df, max_columns=3)

    # Display results
    print("Columns with Mostly Unique Values:", highly_unique_identifiers, "\n")

    return consistency_report, composite_keys
