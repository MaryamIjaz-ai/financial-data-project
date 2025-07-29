import pandas as pd
import openpyxl

class ExcelProcessor:
    def __init__(self):
        self.files = {}

    def load_files(self, file_paths):
        for path in file_paths:
            print(f"\nLoading file: {path}")
            xls = pd.ExcelFile(path, engine='openpyxl')
            self.files[path] = {}
            for sheet_name in xls.sheet_names:
                print(f"  -> Reading sheet: {sheet_name}")
                self.files[path][sheet_name] = xls.parse(sheet_name)

    def get_sheet_info(self):
        for path, sheets in self.files.items():
            print(f"\n📁 File: {path}")
            print(f"📄 Sheets found: {len(sheets)}")
            for sheet_name, df in sheets.items():
                print(f"  • Sheet: {sheet_name}")
                print(f"    - Shape: {df.shape}")
                print(f"    - Columns: {list(df.columns)}")

    def extract_data(self, file_path, sheet_name):
        return self.files.get(file_path, {}).get(sheet_name, pd.DataFrame())

    def preview_data(self, file_path, sheet_name, rows=5):
        df = self.extract_data(file_path, sheet_name)
        print(f"\n🔍 Preview of {sheet_name} in {file_path}:\n")
        print(df.head(rows))
