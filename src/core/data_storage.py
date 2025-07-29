import pandas as pd

class FinancialDataStore:
    def __init__(self):
        self.data = {}
        self.indexes = {}
        self.metadata = {}

    def add_dataset(self, name, df, column_types):
        self.data[name] = df
        self.metadata[name] = column_types
        self.indexes[name] = {}

        if 'date' in column_types.values():
            date_cols = [col for col, typ in column_types.items() if typ == 'date']
            if date_cols:
                self.indexes[name]['date'] = df.set_index(date_cols[0], drop=False)

        if 'number' in column_types.values():
            amt_cols = [col for col, typ in column_types.items() if typ == 'number']
            if amt_cols:
                self.indexes[name]['amount'] = df.set_index(amt_cols[0], drop=False)

    def query_by_date_range(self, name, start_date, end_date):
        df = self.indexes.get(name, {}).get('date', None)
        if df is None:
            print(f"No date index available for '{name}'")
            return pd.DataFrame()
        mask = (df.index >= start_date) & (df.index <= end_date)
        return df.loc[mask]

    def query_by_amount_range(self, name, min_amt, max_amt):
        df = self.indexes.get(name, {}).get('amount', None)
        if df is None:
            print(f"No amount index available for '{name}'")
            return pd.DataFrame()
        mask = (df.index >= min_amt) & (df.index <= max_amt)
        return df.loc[mask]

    def aggregate_data(self, name, group_by_column, agg_column, agg_func='sum'):
        df = self.data.get(name)
        if df is None:
            print(f"No dataset named '{name}'")
            return pd.DataFrame()
        if group_by_column not in df.columns or agg_column not in df.columns:
            print("Invalid column names for aggregation.")
            return pd.DataFrame()
        return df.groupby(group_by_column)[agg_column].agg(agg_func).reset_index()
