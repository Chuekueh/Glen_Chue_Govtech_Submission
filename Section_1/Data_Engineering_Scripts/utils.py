import pandas as pd
from datetime import datetime
from dateutil import parser
from dateutil.parser import ParserError
from dateutil.relativedelta import relativedelta
import hashlib

def add_in_cols (df):
    df['first_name'] = ""
    df['last_name'] = ""
    df['above_18'] = False 
    df['membership_id'] = ""
    df['is_succesful'] = False
    return df 

def process_dob(date_str):
    try:
        return parser.parse(date_str).strftime('%Y%m%d')
    except ParserError as e:
        print(f'ERROR for dob value {date_str}:', e) 
        return pd.NaT
    
def is_18_years_old(date_str):
    try:
        date_of_birth = parser.parse(date_str)
        eighteen_years_ago = pd.Timestamp.now() - relativedelta(years=18)
        return date_of_birth <= eighteen_years_ago
    except TypeError as e:
        print(f'ERROR for dob value {date_str}:', e) 
        return False

def succesful_application(row):
    has_name = bool(row['name'])
    has_eight_digits_handphone = bool(str(row['mobile_no']).isdigit() and len(str(row['mobile_no'])) == 8)
    has_valid_email = row['email'].endswith(('.com', '.net'))
    is_above_18 = row['above_18']
    return has_name and has_eight_digits_handphone and is_above_18 and has_valid_email

def generate_membership_id(row):
    last_name = row['last_name']
    dob = row['date_of_birth']
    hashed_birthday = hashlib.sha256(dob.encode()).hexdigest()[:5]
    return f'{last_name}_{hashed_birthday}'
    
def enforce_data_types(df, column_data_types):
    for column, data_type in column_data_types.items():
        if data_type == 'int':
            df[column] = pd.to_numeric(df[column], errors='coerce', downcast='integer')
        elif data_type == 'float':
            df[column] = pd.to_numeric(df[column], errors='coerce', downcast='float')
        elif data_type == 'datetime':
            df[column] = pd.to_datetime(df[column], errors='coerce')
        elif data_type == 'timedelta':
            df[column] = pd.to_timedelta(df[column], errors='coerce')
        elif data_type == 'str':
            df[column] = df[column].astype(str)
        else:
            raise ValueError(f"Invalid data type '{data_type}' specified for column '{column}'.")

    return df
    


