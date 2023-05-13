import os
from ML_func import * 
import pandas as pd

def train_models(dir_path, X_train_path, y_train_path, label_encoder_path, encoder_path):
        # Assuming you have the X_train and y_train data for each directory
        
        X_train = pd.read_csv(X_train_path, index_col=0)
        y_train = pd.read_csv(y_train_path, index_col=0)
        
        X_train_encoded, y_train_encoded = encode_categorical(X_train, y_train, label_encoder_path, encoder_path)

        # Find the best Random Forest model
        best_rf_model, best_params = find_best_random_forest(X_train_encoded, y_train_encoded, dir_path)
        
        # Save the best model to the same directory
        model_save_path = os.path.join(dir_path, "best_rf_model.pkl")
        with open(model_save_path, 'wb') as file:
            pickle.dump(best_rf_model, file)
        
        print(f"Best model saved for directory: {dir_name}")
        print("Best Parameters:", best_params)
     


if __name__ == "__main__":
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


            train_models(dir_path, X_train_path, y_train_path, label_encoder_path, encoder_path)



