import sqlite3
import pandas as pd

def load_sql_file_to_dataframe(db_file_path):
    """
    Execute an SQL query on an SQLite database and return the result as a Pandas DataFrame.

    :param db_file_path: Path to the SQLite database file.
    :return: A Pandas DataFrame containing the results of the SQL query.
    """
    
    sql_query = """
    SELECT * FROM timeseries;
    """
    
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file_path)

    try:
        # Execute the SQL query and load the result into a DataFrame
        dataframe = pd.read_sql_query(sql_query, conn)

        print("SQL query executed successfully and data loaded into DataFrame.")
        return dataframe

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    finally:
        # Close the connection
        conn.close()

