import pandas as pd
from config import connect
from logger import setup_logger
from constants import file_name, csv_file

log = setup_logger(__file__)


def sum_amount_by_business(df):
    """Sum Description for each unique instance of Amount."""
    return df.groupby("Amount")["Description"].sum().reset_index()


if __name__ == "__main__":
    """Connect to file_name and open up sheet_name"""
    log.info(f"Connecting to {file_name}")
    conn = connect(file_name)
    log.info("Successfully connected!")

    # worksht = conn.worksheet("title", sheet_name) # Expenses 2024
    worksht = conn.worksheet("title", "test")

    # Create dataframe
    log.info(csv_file)
    print(csv_file)
    df = pd.read_csv(csv_file, header=0)  # Assumes first row contains column names
    print(df.head())

    # Manipulate dataframe
    summed_df = sum_amount_by_business(df)
    print(summed_df)

    worksht.set_dataframe(summed_df, (1, 1))
