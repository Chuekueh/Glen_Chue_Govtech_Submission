from datetime import datetime

def add_in_cols (df):
    df['first_name'] = ""
    df['last_name'] = ""
    df['above_18'] = False 
    df['membership_id'] = ""
    df['succesful'] = False
    df['processed_time'] = datetime.now().strftime('%y%m%d%H')
    return df 