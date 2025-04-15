"""Data writing utilities for Coinvert CSV conversion.

Provides a function to write the output DataFrame to a CSV file in the required format.

Functions:
    write_output_csv: Write a Polars DataFrame to a CSV file, ensuring the output directory exists.

Author: Bjorn Melin
Date: 2025-04-15
"""

from pathlib import Path
import polars as pl


def write_output_csv(df: pl.DataFrame, filepath: str) -> None:
    """Write a Polars DataFrame to a CSV file, ensuring the output directory exists.

    Args:
        df (pl.DataFrame): The DataFrame to write to CSV.
        filepath (str): Path to the output CSV file.

    Returns:
        None

    Raises:
        Exception: If writing the file fails for any reason.
    """
    try:
        output_dir = Path(filepath).parent
        output_dir.mkdir(parents=True, exist_ok=True)
        df.write_csv(filepath, include_bom=False, include_header=True)
        print(f"Output CSV successfully written to '{filepath}'.")
    except Exception as e:
        print(f"Error writing output CSV to '{filepath}': {e}")
        raise
