import os
import json
from ML_func import * 
import pandas as pd

def train_models(dir_path, X_train_path, y_train_path, label_encoder_path, model_path, seed):
        # Assuming you have the X_train and y_train data for each directory
        
        X_train = pd.read_csv(X_train_path, index_col=0)
        y_train = pd.read_csv(y_train_path, index_col=0)
        
        X_train_encoded, y_train_encoded = encode_categorical(X_train, y_train, label_encoder_path, mode='train')

        # Find the best Random Forest model
        if 'rf' in model_path:
            best_rf_model, best_rf_params, best_rf_score = find_best_random_forest(X_train_encoded, y_train_encoded, dir_path, seed)
        
            # Save the best model to the same directory
            with open(model_path, 'wb') as file:
                pickle.dump(best_rf_model, file)

            print(f"Best rf model saved for directory: {dir_name}")
            print("Best rf Parameters:", best_rf_params)
            print("Best rf Score:", best_rf_score)
        
        elif 'svm' in model_path:
            best_svm_model, best_svm_params, best_svm_score = find_best_svm_model(X_train_encoded, y_train_encoded, dir_path, seed)
        
            # Save the best model to the same directory
            with open(model_path, 'wb') as file:
                pickle.dump(best_svm_model, file)
            
            print(f"Best svm model saved for directory: {dir_name}")
            print("Best svm Parameters:", best_svm_params)
            print("Best svm Score:", best_svm_score)
     
def test_models(dir_path, X_test_path, y_test_path, label_encoder_path, model_path, seed, average='weighted'):
     
    X_test = pd.read_csv(X_test_path, index_col=0)
    y_test = pd.read_csv(y_test_path, index_col=0)
    
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    
    # Encode the test data using the loaded encoders
    X_test_encoded , y_test_encoded = encode_categorical(X_test, y_test, label_encoder_path, mode='test')
    
    # Make predictions on the test set
    y_pred = model.predict(X_test_encoded)
    
    # Calculate precision, recall, and F1 score
    precision = precision_score(y_test_encoded, y_pred, average=average)
    recall = recall_score(y_test_encoded, y_pred, average=average)
    f1 = f1_score(y_test_encoded, y_pred, average=average)
    
    return precision, recall, f1

if __name__ == "__main__":
    with open('~/Glen_Chue_Govtech_Submission/Section_5/model_results.json', 'r') as file:
        model_results = json.load(file)

    data_dir = "~/Glen_Chue_Govtech_Submission/Section_5/ML_Data"
    for dir_name in os.listdir(data_dir):
        dir_path = os.path.join(data_dir, dir_name)
        if os.path.isdir(dir_path):
            X_train_path = os.path.join(dir_path, "train_features.csv")
            y_train_path = os.path.join(dir_path, "train_label.csv")
            X_test_path = os.path.join(dir_path, "test_features.csv")
            y_test_path = os.path.join(dir_path, "test_label.csv")

            for seed in [0,42,135]:
                label_encoder_path = os.path.join(dir_path, f"label_encoder_{seed}.pkl")
                model_rf_path = os.path.join(dir_path, f"best_rf_model_{seed}.pkl")
                model_svm_path = os.path.join(dir_path, f"best_svm_model_{seed}.pkl")

                for model_path in [model_rf_path, model_svm_path]:
                    train_models(dir_path, X_train_path, y_train_path, label_encoder_path, model_path, seed)
                    precision, recall, f1 = test_models(dir_path, X_train_path, y_train_path, label_encoder_path, model_path, seed)

                    if model_path not in model_results:
                        model_results[model_path] = {'precision':precision, 
                                    'recall': recall,
                                    'f1': f1,
                                    'label_encoder':label_encoder_path}
    
    with open('~/Glen_Chue_Govtech_Submission/Section_5/model_results.json', 'w') as file:
        json.dump(model_results, file)





