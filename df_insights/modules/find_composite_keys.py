def find_composite_keys(df, max_columns=3):
    from itertools import combinations
    """
    Identifies possible composite keys by testing column combinations for uniqueness.

    Args:
        df (pd.DataFrame): The input dataframe.
        max_columns (int): Maximum number of columns to consider in combinations.

    Returns:
        tuple or None: A tuple containing column names that form a unique key, or None if no composite key is found.
    """
    for num_cols in range(2, max_columns + 1):  # Try pairs, triplets, etc.
        for cols in combinations(df.columns, num_cols):
            if df[list(cols)].drop_duplicates().shape[0] == df.shape[0]:
                print(f"Possible Composite Key Found: {cols}")  # Print the found composite key
                return cols  # Return the first found unique combination

    print("No Possbile composite unique key found.")  # Print if no composite key exists
    return None