import pandas as pd
from config import connect
from logger import setup_logger
from constants import file_name, csv_file, sheet_name

log = setup_logger(__file__)


if __name__ == "__main__":
    """
    Connect to google sheet and write to test tab
    """
    conn = connect(file_name)

    sheet = conn.worksheet("title", sheet_name) # Expenses 2024
    sheet.clear() # clear from last run

    # Create dataframe
    log.info(f"Reading from csv {csv_file}")
    df = pd.read_csv(csv_file, header=0)  # assumes first row contains column names

    df = df[df["Amount"] <= 0] # remove positive amounts (payments)

    # Clean up/group data
    summed_df = df.groupby("Amount")["Description"].sum().reset_index() # sum and group by amount
    # df = df.groupby("Amount").sum().reset_index()

    # Write df to google sheet
    sheet.set_dataframe(df, (1, 1), copy_index=False, copy_head=True)
    log.info(f"Data written to {sheet_name} tab")
