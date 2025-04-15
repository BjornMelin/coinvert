"""Data loading utilities for Coinvert CSV conversion.

Provides functions to load the source transactions CSV
and extract the header from the Turbotax template CSV.

Functions:
    load_source_csv: Load the source transactions CSV as a Polars DataFrame.
    get_template_header: Extract the header (column names) from the template CSV.

Author: Bjorn Melin
Date: 2025-04-15
"""

import polars as pl


def load_source_csv(
    filepath: str, columns_to_use: list[str] | None = None
) -> pl.DataFrame:
    """Load the source transactions CSV file as a Polars DataFrame.

    Args:
        filepath (str): Path to the source CSV file.
        columns_to_use (list[str] | None): Optional list of
            columns to load. If None, load all columns.

    Returns:
        pl.DataFrame: Loaded Polars DataFrame containing the source data.

    Raises:
        FileNotFoundError: If the file does not exist at the given path.
    """
    try:
        df = pl.read_csv(filepath, columns=columns_to_use, infer_schema_length=1000)
    except FileNotFoundError:
        print(
            f"Error: Source CSV file not found at '{filepath}'. "
            "Please check SOURCE_CSV_PATH in config.py."
        )
        raise
    return df


def get_template_header(filepath: str) -> list[str]:
    """Extract the header (column names) from the template CSV file.

    Args:
        filepath (str): Path to the template CSV file.

    Returns:
        list[str]: List of column names from the template CSV.

    Raises:
        FileNotFoundError: If the file does not exist at the given path.
    """
    try:
        header_df = pl.read_csv(filepath, n_rows=0)
    except FileNotFoundError:
        print(
            "Error: Template CSV file not found at "
            f"'{filepath}'. Please check TEMPLATE_CSV_PATH in config.py."
        )
        raise
    return header_df.columns
