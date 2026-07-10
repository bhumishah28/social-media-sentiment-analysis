import pandas as pd

COLUMN_NAMES = [
    "target",
    "id",
    "date",
    "flag",
    "user",
    "text"
]

def load_data(file_path):
    df = pd.read_csv(
        file_path,
        encoding="latin-1",
        header=None,
        names=COLUMN_NAMES
    )

    return df



