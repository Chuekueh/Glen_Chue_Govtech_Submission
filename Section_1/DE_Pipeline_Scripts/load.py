import os
import pandas as pd 
from constants import *
from utils import enforce_data_types

def data_load():

    files = [os.path.join(EXTRACT_DIR, f) for f in os.listdir(TRANSFORM_DIR) if os.path.isfile(os.path.join(TRANSFORM_DIR, f))]

    for file in files:
        try:
            print(f"Preparing data from {file} for Loading")
            data = pd.read_csv(file)
            print("Enforcing Datatypes")
            data = enforce_data_types(data, column_data_types)

            if "succesfil_applicants" in os.path.basename(file):
                print(f"Saving cleaned succesful applicants data to {SUCCESFUL_LOAD_DIR}/{os.path.basename(file)}_final")
                data.to_csv(f"{SUCCESFUL_LOAD_DIR}/{os.path.basename(file)}_final", index=False)
            else:
                print(f"Saving cleaned succesful applicants data to {UNSUCCESFUL_LOAD_DIR}/{os.path.basename(file)}_final")
                data.to_csv(f"{UNSUCCESFUL_LOAD_DIR}/{os.path.basename(file)}_final")

            os.remove(file)
            print(f"Removed {file} as successfully transformed to load state")

        except Exception as e:
            raise e

if __name__ == "__main__":
    data_load ()