"""Configuration for Coinvert CSV conversion.

Defines file paths, column mappings, and constants for the conversion process.

Variables:
    SOURCE_CSV_PATH: Path to the input/source transactions CSV file.
    TEMPLATE_CSV_PATH: Path to the Turbotax template CSV file.
    OUTPUT_CSV_PATH: Path to the output CSV file for Turbotax upload.
    TURBOTAX_COLUMNS: List of column names required by the Turbotax template.
    SOURCE_COLUMN_MAP: Mapping from source CSV columns to template columns.
    TYPE_MAPPING: Mapping from source transaction types to Turbotax types.
    DATE_FORMAT: Date format string for parsing source dates.

Author: Bjorn Melin
Date: 2025-04-15
"""

# Path to the input/source transactions CSV file
SOURCE_CSV_PATH: str = "data/source_transactions.csv"

# Path to the Turbotax template CSV file
TEMPLATE_CSV_PATH: str = "data/Custom_CSV_Template.csv"

# Path to the output CSV file for Turbotax upload
OUTPUT_CSV_PATH: str = "output/turbotax_upload.csv"

# List of column names required by the Turbotax template
TURBOTAX_COLUMNS: list[str] = [
    "Date",
    "Type",
    "Sent Asset",
    "Sent Amount",
    "Received Asset",
    "Received Amount",
    "Fee Asset",
    "Fee Amount",
    "Market Value Currency",
    "Market Value",
    "Description",
    "Transaction Hash",
    "Transaction ID",
]

# Mapping from source CSV columns to template columns (to be filled by user)
SOURCE_COLUMN_MAP: dict[str, str] = {}

# Mapping from source transaction types to Turbotax types (to be filled by user)
TYPE_MAPPING: dict[str, str] = {}

# Date format string for parsing source dates (to be filled by user)
DATE_FORMAT: str = ""
