import re
import pandas as pd
from datetime import datetime, timedelta

class FormatParser:
    def __init__(self):
        pass

    def parse_amount(self, value):
        if pd.isnull(value):
            return None
        value = str(value).strip()
        if re.match(r'^\(\s*[\d,\.]+\s*\)$', value):
            value = '-' + value.replace('(', '').replace(')', '')
        if value.endswith('-'):
            value = '-' + value[:-1]
        value = re.sub(r'[^\d\.\-KMBkmb]', '', value)
        multiplier = 1
        if value.lower().endswith('k'):
            multiplier = 1_000
            value = value[:-1]
        elif value.lower().endswith('m'):
            multiplier = 1_000_000
            value = value[:-1]
        elif value.lower().endswith('b'):
            multiplier = 1_000_000_000
            value = value[:-1]
        try:
            return float(value) * multiplier
        except:
            return None

    def parse_date(self, value):
        if pd.isnull(value):
            return None
        value = str(value).strip()
        if re.match(r'^\d{5}$', value):
            try:
                base_date = datetime(1899, 12, 30)
                return (base_date + timedelta(days=int(value))).date()
            except:
                return None
        q_match = re.match(r'Q([1-4])[\s\-]?(\d{2,4})', value, re.IGNORECASE)
        if q_match:
            q, y = int(q_match.group(1)), q_match.group(2)
            year = int("20" + y) if len(y) == 2 else int(y)
            month = (q - 1) * 3 + 1
            return datetime(year, month, 1).date()
        date_formats = [
            "%Y-%m-%d", "%m/%d/%Y", "%d/%m/%Y", "%d-%b-%Y", "%b %Y", "%B %Y", "%d-%m-%Y", "%d.%m.%Y"
        ]
        for fmt in date_formats:
            try:
                return datetime.strptime(value, fmt).date()
            except:
                continue
        return None
