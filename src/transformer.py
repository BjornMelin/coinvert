"""Data transformation logic for Coinvert CSV conversion.

Provides the core function to transform the loaded
source DataFrame according to configuration rules.

Functions:
    transform_data: Apply column renaming and future transformations to the input DataFrame.

Author: Bjorn Melin
Date: 2025-04-15
"""

import polars as pl
import polars.exceptions as pl_exceptions
import config


def transform_data(df: pl.DataFrame) -> pl.DataFrame:
    """Transform the input DataFrame according to config rules.

    Performs column renaming, date conversion, and type mapping as initial transformation steps.

    Args:
        df (pl.DataFrame): The input DataFrame loaded from the source CSV.

    Returns:
        pl.DataFrame: The transformed DataFrame with renamed and mapped columns.

    Raises:
        KeyError: If a column specified in SOURCE_COLUMN_MAP is not found in the DataFrame.
        pl_exceptions.ComputeError: If date parsing fails for all rows.
    """
    try:
        df = df.rename(config.SOURCE_COLUMN_MAP)
    except KeyError as e:
        print(
            f"Error: Column '{e.args[0]}' specified in SOURCE_COLUMN_MAP not found in source data. "
            "Please check your config.py and source CSV."
        )
        raise

    try:
        df = df.with_columns(
            [
                pl.col("datetime")
                .str.strptime(pl.Datetime, format=config.DATE_FORMAT, strict=False)
                .dt.strftime("%-m/%-d/%Y %H:%M")
                .alias("Date"),
                pl.col("source_type")
                .map_dict(config.TYPE_MAPPING, default=pl.lit("Unknown"))
                .alias("Type"),
            ]
        )
    except pl_exceptions.ComputeError:
        print(
            "Error: Failed to parse dates in 'datetime' column. "
            "Check DATE_FORMAT in config.py and source data values."
        )
        raise

    return df
