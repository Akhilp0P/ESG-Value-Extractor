import pandas as pd
import os

def export_to_csv(data_list: list, output_path: str):
    """
    Converts a list of result dictionaries into a CSV file.
    """
    if not data_list:
        print("No data to export.")
        return

    df = pd.DataFrame(data_list)
    df.to_csv(output_path, index=False)
    print(f"Results successfully exported to: {output_path}")
