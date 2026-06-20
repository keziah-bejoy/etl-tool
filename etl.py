import pandas as pd
from dateutil.parser import parse
import os
import re
from dotenv import load_dotenv

load_dotenv(override=True)

# File paths
INPUT = os.getenv('INPUT_FILE')
OUTPUT = os.getenv('OUTPUT_FILE')
REPORT = os.getenv('REPORT_FILE')

# Validation lists
VALID_GENDERS = os.getenv('VALID_GENDERS').split(',')
VALID_STATUS = os.getenv('VALID_STATUS').split(',')

# Threshold
THRESHOLD = int(os.getenv('THRESHOLD'))

# Range values
AGE_MIN = int(os.getenv('AGE_MIN'))
AGE_MAX = int(os.getenv('AGE_MAX'))
SALARY_MIN = int(os.getenv('SALARY_MIN'))
SALARY_MAX = int(os.getenv('SALARY_MAX'))
QUANTITY_MIN = int(os.getenv('QUANTITY_MIN'))
QUANTITY_MAX = int(os.getenv('QUANTITY_MAX'))
PRICE_MIN = int(os.getenv('PRICE_MIN'))
PRICE_MAX = int(os.getenv('PRICE_MAX'))

# Column keywords
EMAIL_KEYWORDS = os.getenv('EMAIL_KEYWORDS').split(',')
PHONE_KEYWORDS = os.getenv('PHONE_KEYWORDS').split(',')
DEPARTMENT_KEYWORDS = os.getenv('DEPARTMENT_KEYWORDS').split(',')
AGE_KEYWORDS = os.getenv('AGE_KEYWORDS').split(',')
SALARY_KEYWORDS = os.getenv('SALARY_KEYWORDS').split(',')
NAME_KEYWORDS = os.getenv('NAME_KEYWORDS').split(',')
DATE_KEYWORDS = os.getenv('DATE_KEYWORDS').split(',')
URL_KEYWORDS = os.getenv('URL_KEYWORDS').split(',')
ZIPCODE_KEYWORDS = os.getenv('ZIPCODE_KEYWORDS').split(',')
GENDER_KEYWORDS = os.getenv('GENDER_KEYWORDS').split(',')
STATUS_KEYWORDS = os.getenv('STATUS_KEYWORDS').split(',')
CITY_KEYWORDS = os.getenv('CITY_KEYWORDS').split(',')
COUNTRY_KEYWORDS = os.getenv('COUNTRY_KEYWORDS').split(',')
PRODUCT_ID_KEYWORDS = os.getenv('PRODUCT_ID_KEYWORDS').split(',')
QUANTITY_KEYWORDS = os.getenv('QUANTITY_KEYWORDS').split(',')
PRICE_KEYWORDS = os.getenv('PRICE_KEYWORDS').split(',')

#regex patterns
EMAIL_PATTERN = os.getenv('EMAIL_PATTERN')
PHONE_PATTERN = os.getenv('PHONE_PATTERN')
DATE_PATTERN = os.getenv('DATE_PATTERN')
URL_PATTERN = os.getenv('URL_PATTERN')
ZIPCODE_PATTERN = os.getenv('ZIPCODE_PATTERN')

# COLUMN KEYWORDS DICTIONARY
column_keywords = {
    'email': EMAIL_KEYWORDS,
    'phone': PHONE_KEYWORDS,
    'department': DEPARTMENT_KEYWORDS,
    'age': AGE_KEYWORDS,
    'salary': SALARY_KEYWORDS,
    'name': NAME_KEYWORDS,
    'date': DATE_KEYWORDS,
    'url': URL_KEYWORDS,
    'zipcode': ZIPCODE_KEYWORDS,
    'gender': GENDER_KEYWORDS,
    'status': STATUS_KEYWORDS,
    'city': CITY_KEYWORDS,
    'country': COUNTRY_KEYWORDS,
    'product_id': PRODUCT_ID_KEYWORDS,
    'quantity': QUANTITY_KEYWORDS,
    'price': PRICE_KEYWORDS
}


# FILE READING FUNCTION (Supports CSV, XLSX, JSON)
def read_file(filename):
    extension = filename.split('.')[-1].lower()
    
    if extension == 'csv':
        df = pd.read_csv(filename)
    elif extension == 'xlsx':
        df = pd.read_excel(filename, dtype=str)
    elif extension == 'json':
        df = pd.read_json(filename)
    else:
        print(f"Unsupported file type: {extension}")
        return None
    
    return df


# FILE SAVING FUNCTION

def save_file(df, filename):
    extension = filename.split('.')[-1].lower()
    
    if extension == 'csv':
        df.to_csv(filename, index=False)
    elif extension == 'xlsx':
        df.to_excel(filename, index=False)
    elif extension == 'json':
        df.to_json(filename, orient='records', indent=2)
    else:
        print(f"Unsupported file type for saving: {extension}")
        return False
    
    return True

# READ INPUT FILE
df = read_file(INPUT)
if df is None:
    exit()

original = len(df)
df = df.drop_duplicates()
duplicated = original - len(df)


# DATA DETECTION FUNCTIONS
def is_email(column):
    non_null = column.dropna()
    if len(non_null) == 0:
        return False
    count = 0
    for value in non_null:
        if re.match(EMAIL_PATTERN, str(value)):
            count += 1
    percentage = (count / len(non_null)) * 100
    return percentage >= THRESHOLD

def is_phone(column):
    non_null = column.dropna()
    if len(non_null) == 0:
        return False
    count = 0
    for value in non_null:
        if re.match(PHONE_PATTERN, str(value)):
            count += 1
    percentage = (count / len(non_null)) * 100
    return percentage >= THRESHOLD

def is_date(column):
    non_null = column.dropna()
    if len(non_null) == 0:
        return False
    count = 0
    for value in non_null:
        if re.match(DATE_PATTERN, str(value)):
            count += 1
    percentage = (count / len(non_null)) * 100
    return percentage >= THRESHOLD

def is_age(column):
    non_null = column.dropna()
    if len(non_null) == 0:
        return False
    count = 0
    for value in non_null:
        try:
            age = float(value)
            if AGE_MIN < age < AGE_MAX:
                count += 1
        except:
            pass
    percentage = (count / len(non_null)) * 100
    return percentage >= THRESHOLD

def is_salary(column):
    non_null = column.dropna()
    if len(non_null) == 0:
        return False
    count = 0
    for value in non_null:
        try:
            salary = float(value)
            if SALARY_MIN <= salary <= SALARY_MAX:
                count += 1
        except:
            pass
    percentage = (count / len(non_null)) * 100
    return percentage >= THRESHOLD

def is_numeric(column):
    non_null = column.dropna()
    if len(non_null) == 0:
        return False
    count = 0
    for value in non_null:
        try:
            float(str(value))
            count += 1
        except:
            pass
    percentage = (count / len(non_null)) * 100
    return percentage >= THRESHOLD

def is_url(column):
    non_null = column.dropna()
    if len(non_null) == 0:
        return False
    count = 0
    for value in non_null:
        if re.match(URL_PATTERN, str(value)):
            count += 1
    percentage = (count / len(non_null)) * 100
    return percentage >= THRESHOLD

def is_zipcode(column):
    non_null = column.dropna()
    if len(non_null) == 0:
        return False
    count = 0
    for value in non_null:
        if re.match(ZIPCODE_PATTERN, str(value)):
            count += 1
    percentage = (count / len(non_null)) * 100
    return percentage >= THRESHOLD

def is_gender(column):
    non_null = column.dropna()
    if len(non_null) == 0:
        return False
    count = 0
    for value in non_null:
        if str(value).lower() in VALID_GENDERS:
            count += 1
    percentage = (count / len(non_null)) * 100
    return percentage >= THRESHOLD

def is_status(column):
    non_null = column.dropna()
    if len(non_null) == 0:
        return False
    count = 0
    for value in non_null:
        if str(value).lower() in VALID_STATUS:
            count += 1
    percentage = (count / len(non_null)) * 100
    return percentage >= THRESHOLD

def is_quantity(column):
    non_null = column.dropna()
    if len(non_null) == 0:
        return False
    count = 0
    for value in non_null:
        try:
            qty = float(value)
            if qty > 0 and qty.is_integer() and QUANTITY_MIN <= qty <= QUANTITY_MAX:
                count += 1
        except:
            pass
    percentage = (count / len(non_null)) * 100
    return percentage >= THRESHOLD

def is_price(column):
    non_null = column.dropna()
    if len(non_null) == 0:
        return False
    count = 0
    for value in non_null:
        try:
            price = float(value)
            if PRICE_MIN <= price <= PRICE_MAX:
                count += 1
        except:
            pass
    percentage = (count / len(non_null)) * 100
    return percentage >= THRESHOLD

#COLUMN DETECTION
email_col = None
phone_col = None
department_col = None
age_col = None
salary_col = None
name_col = None
date_col = None
url_col = None
zipcode_col = None
gender_col = None
status_col = None
city_col = None
country_col = None
product_id_col = None
quantity_col = None
price_col = None

for col in df.columns:
    col_lower = col.lower()
    
    # 1. Email
    if email_col is None:
        name_match = any(kw in col_lower for kw in column_keywords['email'])
        data_match = is_email(df[col])
        if name_match or data_match:
            email_col = col
    
    # 2. Phone: 
    if phone_col is None:
        name_match = any(kw in col_lower for kw in column_keywords['phone'])
        data_match = is_phone(df[col])
        if name_match or data_match:
            phone_col = col
    
    # 3. Date:
    if date_col is None:
        name_match = any(kw in col_lower for kw in column_keywords['date'])
        data_match = is_date(df[col])
        if name_match and data_match:
            date_col = col
    
    # 4. Age: 
    if age_col is None:
         name_match = any(kw in col_lower for kw in column_keywords['age'])
         data_match = is_age(df[col])
         if name_match and data_match:
            age_col = col
    
    # 5. Gender: 
    if gender_col is None:
        name_match = any(kw in col_lower for kw in column_keywords['gender'])
        data_match = is_gender(df[col])
        if name_match or data_match:
            gender_col = col
    
    # 6. Status:
    if status_col is None:
        name_match = any(kw in col_lower for kw in column_keywords['status'])
        data_match = is_status(df[col])
        if name_match or data_match:
            status_col = col
    
    # 7. URL: 
    if url_col is None:
        name_match = any(kw in col_lower for kw in column_keywords['url'])
        data_match = is_url(df[col])
        if name_match or data_match:
            url_col = col
    
    # 8. Quantity: 
    if quantity_col is None:
        name_match = any(kw in col_lower for kw in column_keywords['quantity'])
        data_match = is_quantity(df[col])
        if name_match and data_match:
            quantity_col = col
    
    # 9. Price: 
    if price_col is None:
        name_match = any(kw in col_lower for kw in column_keywords['price'])
        data_match = is_price(df[col])
        if name_match and data_match:
            price_col = col
    
    # 10. Salary: 
    if salary_col is None:
        name_match = any(kw in col_lower for kw in column_keywords['salary'])
        data_match = is_salary(df[col])
        if name_match and data_match:
            salary_col = col
    
    # 11. Zipcode: 
    if zipcode_col is None:
        name_match = any(kw in col_lower for kw in column_keywords['zipcode'])
        data_match = is_zipcode(df[col])
        if name_match and data_match:
            zipcode_col = col
    
    # 12. Name:
    if name_col is None:
        name_match = any(kw in col_lower for kw in column_keywords['name'])
        if name_match:
            name_col = col
    
    # 13. Department: 
    if department_col is None:
        name_match = any(kw in col_lower for kw in column_keywords['department'])
        if name_match:
            department_col = col
    
    # 14. City: 
    if city_col is None:
        name_match = any(kw in col_lower for kw in column_keywords['city'])
        if name_match:
            city_col = col
    
    # 15. Country: 
    if country_col is None:
        name_match = any(kw in col_lower for kw in column_keywords['country'])
        if name_match:
            country_col = col
    
    # 16. Product ID:
    if product_id_col is None:
        name_match = any(kw in col_lower for kw in column_keywords['product_id'])
        if name_match:
            product_id_col = col

# Print detected columns 
print("\n" + "-"*50)
print("DETECTED COLUMNS")
print("-"*50)
if email_col:
    print(f"Email: {email_col}")
if phone_col:
    print(f"Phone: {phone_col}")
if department_col:
    print(f"Department: {department_col}")
if age_col:
    print(f"Age: {age_col}")
if salary_col:
    print(f"Salary: {salary_col}")
if name_col:
    print(f"Name: {name_col}")
if date_col:
    print(f"Date: {date_col}")
if url_col:
    print(f"URL: {url_col}")
if zipcode_col:
    print(f"Zipcode: {zipcode_col}")
if gender_col:
    print(f"Gender: {gender_col}")
if status_col:
    print(f"Status: {status_col}")
if city_col:
    print(f"City: {city_col}")
if country_col:
    print(f"Country: {country_col}")
if product_id_col:
    print(f"Product ID: {product_id_col}")
if quantity_col:
    print(f"Quantity: {quantity_col}")
if price_col:
    print(f"Price: {price_col}")
print("-"*50 + "\n")


# NUMERIC CONVERSION
if age_col is not None:
    df[age_col] = pd.to_numeric(df[age_col], errors='coerce')
if salary_col is not None:
    df[salary_col] = pd.to_numeric(df[salary_col], errors='coerce')
if quantity_col is not None:
    df[quantity_col] = pd.to_numeric(df[quantity_col], errors='coerce')
if price_col is not None:
    df[price_col] = pd.to_numeric(df[price_col], errors='coerce')
if zipcode_col is not None:
    df[zipcode_col] = pd.to_numeric(df[zipcode_col], errors='coerce')


# DATE STANDARDIZATION
if date_col is not None:
    def safe_parse_date(date_val):
        if pd.isna(date_val):
            return None
        try:
            return parse(str(date_val))
        except:
            return None
    
    df[date_col] = df[date_col].apply(safe_parse_date)
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    df[date_col] = df[date_col].dt.strftime('%Y-%m-%d')


# VALIDATION
def check_row(row):
    problems = []
    
    # Email
    if email_col is not None:
        email = row[email_col]
        if pd.notna(email):
            if not re.match(EMAIL_PATTERN, str(email)):
                problems.append("Invalid email")
        else:
            problems.append("Unknown email")
    
    # Phone
    if phone_col is not None:
        phone = str(row[phone_col])
        if phone == "0000000000":
            problems.append("Missing phone number")
        elif not re.match(PHONE_PATTERN, phone):
            problems.append("Invalid phone number")
    
    # Department
    if department_col is not None:
        department = row[department_col]
        if pd.isna(department) or department == "Unknown":
            problems.append("Unknown department")
    
    # Age 
    if age_col is not None:
        age = row[age_col]      
        try:
            if pd.isna(age):
                problems.append("Missing age")
            elif age <= AGE_MIN or age >= AGE_MAX:
                problems.append("Invalid age")
        except:
            problems.append("Invalid age (non-numeric)")
    
    # Salary
    if salary_col is not None:
        salary = row[salary_col]
        try:
            if pd.isna(salary):
                problems.append("Missing salary")
            elif salary < 0:
                problems.append("Invalid salary (negative)")
        except:
            problems.append("Invalid salary (non-numeric)")
    
    # Name 
    if name_col is not None:
        name = row[name_col]
        if pd.isna(name) or name == "Unknown":
            problems.append("Unknown name")
    
    # Date
    if date_col is not None:
        date = row[date_col]
        if pd.notna(date):
            if not re.match(DATE_PATTERN, str(date)):
                problems.append("Invalid date format")
        else:
            problems.append("Missing date")
    
    # URL
    if url_col is not None:
        url = row[url_col]
        if pd.notna(url):
            if not re.match(URL_PATTERN, str(url)):
                problems.append("Invalid URL")
        else:
            problems.append("Missing URL")
    
    # Zipcode
    if zipcode_col is not None:
        zipcode = row[zipcode_col]
        if pd.notna(zipcode):
            if not re.match(ZIPCODE_PATTERN, str(zipcode)):
                problems.append("Invalid zipcode")
        else:
            problems.append("Missing zipcode")
    
    # Gender 
    if gender_col is not None:
        gender = row[gender_col]
        if pd.notna(gender):
            gender_str = str(gender).lower()
            if gender_str not in VALID_GENDERS:
                problems.append("Invalid gender")
        else:
            problems.append("Missing gender")
    
    # Status 
    if status_col is not None:
        status = row[status_col]
        if pd.notna(status):
            status_str = str(status).lower()
            if status_str not in VALID_STATUS:
                problems.append("Invalid status")
        else:
            problems.append("Missing status")
    
    # City
    if city_col is not None:
        city = row[city_col]
        if pd.isna(city) or str(city).strip() == "":
            problems.append("Missing city")
    
    # Country 
    if country_col is not None:
        country = row[country_col]
        if pd.isna(country) or str(country).strip() == "":
            problems.append("Missing country")
    
    # Product ID 
    if product_id_col is not None:
        product_id = row[product_id_col]
        if pd.isna(product_id) or str(product_id).strip() == "":
            problems.append("Missing product ID")
    
    # Quantity
    if quantity_col is not None:
        qty = row[quantity_col]
        try:
            if pd.isna(qty):
                problems.append("Missing quantity")
            elif qty < 0:
                problems.append("Invalid quantity (negative)")
        except:
            problems.append("Invalid quantity (non-numeric)")
    
    # Price
    if price_col is not None:
        price = row[price_col]
        try:
            if pd.isna(price):
                problems.append("Missing price")
            elif price < 0:
                problems.append("Invalid price (negative)")
        except:
            problems.append("Invalid price (non-numeric)")
    
    if len(problems) == 0:
        return "No issues"
    else:
        return " | ".join(problems)

df['issues'] = df.apply(check_row, axis=1)


# COLLECT MISSING DATA FOR REPORT
missing_rows = {}
for col in df.columns:
    if col != 'issues':
        missing = df[col].isna()
        rows = df[missing].index.tolist()
        if rows:
            missing_rows[col] = rows


# FILL MISSING VALUES
text_cols = df.select_dtypes(include=['object']).columns
df[text_cols] = df[text_cols].fillna("Unknown")
number_cols = df.select_dtypes(include=['number']).columns
df[number_cols] = df[number_cols].fillna(0)


# ENHANCED REPORT
rows_with_issues = (df['issues'] != "No issues").sum()
total_rows = len(df)
clean_rows = total_rows - rows_with_issues

# Get row numbers for each issue type
issue_rows = {}
for rownum, issues in enumerate(df['issues']):
    if issues != "No issues":
        issue_list = issues.split(' | ')
        for issue in issue_list:
            if issue not in issue_rows:
                issue_rows[issue] = []
            issue_rows[issue].append(rownum)

# Write enhanced report
with open(REPORT, "w") as f:
    f.write("-"*60 + "\n")
    f.write("                    ETL QUALITY REPORT\n")
    f.write("-"*60 + "\n\n")
    
    # 1.SUMMARY
    f.write("SUMMARISED REPORT:\n")
    
    f.write(f"  Original rows:                 {original}\n")
    f.write(f"  Duplicate rows removed:        {duplicated}\n")
    f.write(f"  Rows after cleaning:           {len(df)}\n")
    f.write(f"  Rows with issues:              {rows_with_issues}\n")
    f.write(f"  Clean rows:                    {clean_rows}\n")
    f.write("\n")
    
    # 2. DUPLICATES REMOVED
    if duplicated > 0:
        f.write("DUPLICATES REMOVED\n")
        f.write("-"*60 + "\n")
        f.write(f"  Total duplicates removed: {duplicated}\n")
        f.write("\n")
    
    # 3. MISSING DATA FOUND (with row numbers)
    f.write("MISSING DATA FOUND\n")
    f.write("-"*60 + "\n")
    if missing_rows:
        for col, rows in missing_rows.items():
            f.write(f"  {col} ({len(rows)} rows)\n")
            f.write(f"    Row numbers: {rows}\n")
            f.write("\n")
    else:
        f.write(" No missing data found\n")
        f.write("\n")
    
    # 4. INVALID DATA FOUND (with row numbers)
    f.write("INVALID DATA FOUND\n")
    f.write("-"*60 + "\n")
    if issue_rows:
        for issue, rows in issue_rows.items():
            f.write(f"  {issue} ({len(rows)} rows)\n")
            f.write(f"    Row numbers: {rows}\n")
            f.write("\n")
    else:
        f.write("No invalid data found\n")
        f.write("\n")
    
    # 5. DATA FIXES APPLIED
    f.write("DATA FIXES APPLIED\n")
    f.write("-"*60 + "\n")
    f.write("  Missing text values -> 'Unknown'\n")
    f.write("  Missing number values -> 0\n")
    f.write("  Invalid dates -> Standardized to YYYY-MM-DD\n")
    if duplicated > 0:
        f.write(f"  Duplicates -> {duplicated} rows removed\n")
    else:
        f.write("  No duplicates found\n")
    f.write("\n")
    
# SAVE OUTPUT FILE
save_file(df, OUTPUT)
print("Done!")
print(f"Report saved to: {REPORT}")
