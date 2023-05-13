import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import f1_score, make_scorer, precision_score, recall_score,

def find_best_random_forest(X, y, path):
    # Define the parameter grid for Random Forest
    param_grid = {
        'n_estimators': [100, 200, 300],  # Number of trees in the forest
        'max_depth': [None, 5, 10],       # Maximum depth of each tree
        'min_samples_split': [2, 5, 10],  # Minimum number of samples required to split an internal node
        'min_samples_leaf': [1, 2, 4]     # Minimum number of samples required to be at a leaf node
    }
    
    # Create a Random Forest classifier
    rf_classifier = RandomForestClassifier(random_state=42)
    
    # Define the scoring metric (f1_score in this case)
    scoring_metric = make_scorer(f1_score)
    
    # Perform grid search to find the best configuration 
    grid_search = GridSearchCV(rf_classifier, param_grid, cv=3, scoring=scoring_metric) ## CV = 3 to improve robustness of results
    grid_search.fit(X, y)
    
    # Get the best model and its parameters
    best_model = grid_search.best_estimator_
    best_params = grid_search.best_params_

     # Save the best model to a file
    with open(path, 'wb') as file:
        pickle.dump(best_model, file)
    
    # Fit the best model on the entire dataset
    best_model.fit(X, y)
    
    # Print the best parameters
    print("Best Parameters:", best_params)

    return best_model

def evaluate_model(X_test, y_test, model):
    # Make predictions on the test set
    y_pred = model.predict(X_test)
    
    # Calculate precision, recall, and F1 score
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    print("Precision:", precision)
    print("Recall:", recall)
    print("F1 Score:", f1)

def predict_with_model(X, model):
    # Make predictions using the best model
    predictions = model.predict(X)
    
    return predictions