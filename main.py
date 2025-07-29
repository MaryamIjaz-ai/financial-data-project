"""
Main entry point for Financial Data Parser project.
This script loads Excel files, detects column types, normalizes formats,
stores data using optimized structures, and runs test queries and aggregations.
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from core.excel_processor import ExcelProcessor
from core.type_detector import DataTypeDetector
from core.format_parser import FormatParser
from core.data_storage import FinancialDataStore
from datetime import datetime

# Step 1: Load Excel files
file_paths = [
    r"C:\Users\HP\Downloads\financial-data-analyzer-updated\data\KH_Bank.XLSX",
    r"C:\Users\HP\Downloads\financial-data-analyzer-updated\data\Customer_Ledger_Entries_FULL.xlsx"
]

processor = ExcelProcessor()
processor.load_files(file_paths)
processor.get_sheet_info()

# Step 2: Choose a specific file and sheet
selected_file = file_paths[0]
sheet_name = "Sheet1"  # Replace with actual sheet name from KH_Bank.XLSX
df = processor.extract_data(selected_file, sheet_name)
processor.preview_data(selected_file, sheet_name, rows=5)

# Step 3: Detect column types
detector = DataTypeDetector()
column_types = {}
for col in df.columns:
    result = detector.detect_column_type(df[col])
    column_types[col] = result['type']

print("\n🔎 Detected Column Types:")
print(column_types)

# Step 4: Normalize amounts and dates using FormatParser
parser = FormatParser()
for col, col_type in column_types.items():
    if col_type == 'date':
        df[col] = df[col].apply(parser.parse_date)
    elif col_type == 'number':
        df[col] = df[col].apply(parser.parse_amount)

# Step 5: Store and index data
store = FinancialDataStore()
store.add_dataset("KH_Bank", df, column_types)

# Step 6: Query and aggregate
start = datetime.strptime("2023-01-01", "%Y-%m-%d").date()
end = datetime.strptime("2023-12-31", "%Y-%m-%d").date()

print("\n📅 Filter by Date Range:")
print(store.query_by_date_range("KH_Bank", start, end))

print("\n💰 Filter by Amount Range:")
print(store.query_by_amount_range("KH_Bank", 1000, 10000))

# Replace these column names with actual ones if needed
group_by_col = "Statement.Entry.CreditDebitIndicator"
agg_col = "Statement.Entry.Amount.Value"

print("\n📊 Aggregation Example:")
print(store.aggregate_data("KH_Bank", group_by_column=group_by_col, agg_column=agg_col))
