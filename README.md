# 📊 Financial Data Analyzer

This project is designed to automate the parsing, normalization, and storage of complex financial Excel statements. It supports both structured and semi-structured Excel files such as bank statements and ledger entries.


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


