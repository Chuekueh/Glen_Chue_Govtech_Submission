This is for section 5 of Data Engineering challenge. 

1. EDA.py contains the code that was used to study the input data before deciding what kind of models / sampling was to be utilized for this project. 

2. ML_func.py contains helper functions used throughout this ML Pipeline. 

3. preprocessing.py prepares the feature and label data based on the sampling methods decided from the EDA step. In this case we explored both stratified sampling and normal train-test splitting. 

4. ML_train_test.py is where the ML Models were trained and tested. 

    a. RF and SVC Models were chosen for this project, trained at seed = 0, 42 and 135

    b. label_encoding was carried out on the target column (buying) and the ordinal encoding was utilized to encode the rest of the categorical variables. 

    c. the training logs of the ML Models were stored in ML_training.log files
    d. Model Metadata was stored in model_results.json to allow for easy access of best perfoming historical models in the future. 

5. ML_Predict.py is where the ML Inference is carried out. 