import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor  # Replace with your chosen model
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score  # Import relevant metrics
import joblib  # For saving and loading models

def load_processed_data(file_path):
    """
    Load processed data from a file.
    
    Parameters:
    - file_path: Path to the processed data file.
    
    Returns:
    - df: A pandas DataFrame containing the processed data.
    """
    df = pd.read_csv(file_path)  # Replace with the appropriate data loading code
    return df

def split_data(data, target_column):
    """
    Split data into features and target variables and create a train-test split.
    
    Parameters:
    - data: Processed data as a pandas DataFrame.
    - target_column: The name of the target variable.
    
    Returns:
    - X_train, X_test, y_train, y_test: Split data for training and testing.
    """
    X = data.drop(target_column, axis=1)
    y = data[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):
    """
    Train a machine learning model on the training data.
    
    Parameters:
    - X_train: Features of the training data.
    - y_train: Target variable of the training data.
    
    Returns:
    - model: Trained machine learning model.
    """
    model = RandomForestRegressor()  # Replace with your chosen model
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """
    Evaluate the model's performance on the test data.
    
    Parameters:
    - model: Trained machine learning model.
    - X_test: Features of the test data.
    - y_test: Target variable of the test data.
    """
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    rmse = mse**0.5
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"Mean Squared Error: {mse}")
    print(f"Root Mean Squared Error: {rmse}")
    print(f"Mean Absolute Error: {mae}")
    print(f"R-squared (R2) Score: {r2}")

def save_model(model, model_path):
    """
    Save the trained model to a file.
    
    Parameters:
    - model: Trained machine learning model.
    - model_path: File path to save the model.
    """
    joblib.dump(model, model_path)

def main():
    # Progress: Loading processed data
    data = load_processed_data('processed_data.csv')
    
    # Progress: Splitting data into features and target variables
    target_column_name = 'Net Change'  # Replace with the actual column name
    X_train, X_test, y_train, y_test = split_data(data, target_column_name)
    
    # Progress: Training a machine learning model
    model = train_model(X_train, y_train)
    
    # Progress: Evaluating the model's performance
    evaluate_model(model, X_test, y_test)
    
    # Progress: Saving the trained model for future use
    save_model(model, 'trained_model.pkl')

if __name__ == '__main__':
    main()
