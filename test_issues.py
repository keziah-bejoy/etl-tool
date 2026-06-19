import pandas as pd
from dateutil.parser import parse

df = pd.read_csv('data.csv')
df.columns = df.columns.str.lower().str.strip()
df = df.drop_duplicates()

df['name'] = df['name'].fillna("Unknown")
df['age'] = df['age'].fillna(0)
df['date'] = df['date'].fillna("Unknown")
df['department'] = df['department'].fillna("Unknown")
df['email'] = df['email'].fillna("Unknown")
df['phone'] = df['phone'].fillna("0000000000")

def valid_date(dates):
    if pd.isna(dates) or dates == "Unknown":
        return "Unknown"
    try:
        return parse(str(dates))
    except:
        return "Invalid dates"

df['date'] = df['date'].apply(valid_date)

def check_issues(row):
    problems = []
    if pd.isna(row['name']) or row['name'] == "Unknown":
        problems.append("Unknown")
    age = row['age']
    try:
        if age <= 0 or age >= 120:
            problems.append("Invalid age")
    except:
        problems.append("Non-numeric(invalid)")
    return '|'.join(problems)

# Test on first row
print("Row 0:")
print(df.iloc[0][['name', 'age', 'department', 'phone']])
print("Age type:", type(df.iloc[0]['age']))
print("Issues:", repr(check_issues(df.iloc[0])))
print("\nRow 1 (has missing age):")
print(df.iloc[1][['name', 'age', 'department', 'phone']])
print("Age type:", type(df.iloc[1]['age']))
print("Age value:", repr(df.iloc[1]['age']))
print("Issues:", repr(check_issues(df.iloc[1])))
