from pathlib import Path

file_name = "Finances 2021-2025"
sheet_name = "Expenses 2024"

project_dir = Path(__file__).parent
base_dir = Path(project_dir).parent

csv_file = Path.joinpath(
    base_dir,
    "data",
    "2024_chase_sapphire.CSV"
)