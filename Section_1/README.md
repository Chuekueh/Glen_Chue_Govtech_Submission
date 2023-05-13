This is for section 1 of Data Engineering challenge. 

In this Pipeline, the data is designed to flow from:
    Input_Data --> Archive
    Input_Data --> Extacted_Data --> Transfomed_data --> Succesful_Applications and Unsuccesful_Applications. 

    The archive folder acts as a vault of historical data to allow for easy access should there be a need for data restoration. 

The Scripts Used for this project can be found in DE_Pipeline_Scripts.
    1. constants.py contains the variables that are constantly referenced in the pipeline 
    2. utils.py contain helper functions needed in the pipeline
    3. extract.py extracts the raw data and adds any additional columns needed for downstream processing of data. 
    4. transform.py does data cleaning and normalisation of raw data. 
    5. load.py enforces data_types for every column in the data being ingested and redirects the data to appropriate endpoints. 