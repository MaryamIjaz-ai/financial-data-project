# 📊 Financial Data Analyzer

This project is designed to automate the parsing, normalization, and storage of complex financial Excel statements. It supports both structured and semi-structured Excel files such as bank statements and ledger entries.

---

## 📁 Project Structure

financial-data-analyzer-updated/
│
├── main.py # Main execution file for loading, parsing, and querying data
├── data/
│ ├── Customer_Ledger_Entries_FULL.xlsx
│ └── KH_Bank.XLSX
│
├── src/
│ ├── core/
│ │ ├── init.py
│ │ ├── excel_processor.py # Loads and extracts Excel sheets
│ │ ├── format_parser.py # Normalizes dates and amounts
│ │ ├── data_storage.py # Stores data in SQLite in-memory DB and provides query methods
│ │ └── type_detector.py # Detects column types (amount, date, etc.)
│ │
│ └── tests/
│ ├── init.py
│ ├── test_format_parser.py # Unit tests for amount/date parsing
│ └── test_type_detector.py # Unit tests for type detection
│
└── README.md

## ✅ Features

- 📥 **Loads Excel files** from multiple sheets
- 🔍 **Auto-detects column types** (date, amount, text, etc.)
- 🔄 **Normalizes formats** (amounts, dates)
- 💾 **Stores data** in an SQLite in-memory database
- 📆 **Date range queries** for financial analysis
- 📚 **Unit tests** included for parser and type detection

---

## 🚀 How to Run

1. **Install dependencies**

pip install pandas openpyxl
Run the main script
python main.py
Expected Output

You will see:

Normalized dates and amounts

Type detection summary

Available columns

Query results by date range and aggregated metrics
Run Test Cases
To execute unit tests:
python -m unittest discover src/tests
All tests should pass if everything is set up correctly.
🧠 Technologies Used
Python 3.10+

Pandas

OpenPyXL

SQLite (in-memory)

Unittest (Python’s built-in testing framework)


