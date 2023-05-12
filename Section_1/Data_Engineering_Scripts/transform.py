import pandas as pd 
from constants import *

# obtain ingested data that was processed within the same hour 
raw_data = pd.read_csv(f'{INGEST_DIR}/')