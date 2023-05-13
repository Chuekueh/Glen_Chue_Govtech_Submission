import os
from ML_func import * 
import pandas as pd

def train_models(dir_path, X_train_path, y_train_path, label_encoder_path, encoder_path, model_path):
        # Assuming you have the X_train and y_train data for each directory
        
        X_train = pd.read_csv(X_train_path, index_col=0)
        y_train = pd.read_csv(y_train_path, index_col=0)
        
        X_train_encoded, y_train_encoded = encode_categorical(X_train, y_train, label_encoder_path, encoder_path)

        # Find the best Random Forest model
        best_rf_model, best_params, best_score = find_best_random_forest(X_train_encoded, y_train_encoded, dir_path)
        
        # Save the best model to the same directory
        with open(model_path, 'wb') as file:
            pickle.dump(best_rf_model, file)
        
        print(f"Best model saved for directory: {dir_name}")
        print("Best Parameters:", best_params)
        print("Best Score:", best_score)
     
def test_models(dir_path, X_test_path, y_test_path, label_encoder_path, encoder_path, model_path, average='weighted'):
     
    X_test = pd.read_csv(X_test_path, index_col=0)
    y_test = pd.read_csv(y_test_path, index_col=0)

    with open(encoder_path, 'rb') as file:
        encoder = pickle.load(file)
    
    with open(label_encoder_path, 'rb') as file:
        label_encoder = pickle.load(file)
    
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    
    # Encode the test data using the loaded encoders
    X_test_encoded = encoder.transform(X_test[['maint','doors','persons','lug_boot','safety','class']])
    y_test_encoded = label_encoder.transform(y_test)
    
    # Make predictions on the test set
    y_pred = model.predict(X_test_encoded)
    
    # Calculate precision, recall, and F1 score
    precision = precision_score(y_test_encoded, y_pred, average=average)
    recall = recall_score(y_test_encoded, y_pred, average=average)
    f1 = f1_score(y_test_encoded, y_pred, average=average)
    
    return precision, recall, f1

if __name__ == "__main__":
    model_results = {}

    data_dir = '/Users/glen/Desktop/Glen_Chue_Govtech_Submission/Section_5/ML_Data'
    for dir_name in os.listdir(data_dir):
        dir_path = os.path.join(data_dir, dir_name)
        if os.path.isdir(dir_path):
            X_train_path = os.path.join(dir_path, "train_features.csv")
            y_train_path = os.path.join(dir_path, "train_label.csv")
            X_test_path = os.path.join(dir_path, "test_features.csv")
            y_test_path = os.path.join(dir_path, "test_label.csv")

            label_encoder_path = os.path.join(dir_path, "label_encoder.pkl")
            encoder_path = os.path.join(dir_path, "encoder.pkl")
            model_path = os.path.join(dir_path, "best_rf_model.pkl")

            train_models(dir_path, X_train_path, y_train_path, label_encoder_path, encoder_path, model_path)
            precision, recall, f1 = test_models(dir_path, X_train_path, y_train_path, label_encoder_path, encoder_path, model_path)

            model_results[model_path] = {'precision':precision, 
                                 'recall': recall,
                                 'f1': f1}
    print(model_results)

## While I only tried RF Models in this project, given the data size i think perhaps I should have tried with SVR/SVM which
## require less data for learning. But didnt have the time to add it in.





