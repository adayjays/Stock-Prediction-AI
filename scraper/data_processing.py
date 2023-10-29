import pandas as pd

def load_raw_data(file_path):
    """
    Load raw data from a CSV file.
    
    Parameters:
    - file_path: Path to the raw data CSV file.
    
    Returns:
    - df: A pandas DataFrame containing the raw data.
    """
    df = pd.read_csv(file_path)
    return df

def clean_data(data):
    """
    Clean and preprocess the raw data.
    
    Parameters:
    - data: Raw data as a pandas DataFrame.
    
    Returns:
    - cleaned_data: Processed data with missing values handled, outliers removed, etc.
    """
    # Remove rows with missing values
    cleaned_data = data.dropna()

    # Handle any other data-specific cleaning operations
    # For example, you can convert columns to appropriate data types, remove outliers, etc.

    return cleaned_data

def initial_data_analysis(data):
    """
    Perform initial data analysis to understand the dataset.
    
    Parameters:
    - data: Processed data as a pandas DataFrame.
    """
    # Display the first few rows of the dataset
    print("First few rows of the dataset:")
    print(data.head())

    # Summary statistics of numeric columns
    print("Summary statistics:")
    print(data.describe())

    # Data types and non-null counts
    print("Data types and non-null counts:")
    print(data.info())

    # Additional exploratory analysis as needed

def main():
    # Load raw data from the CSV file
    raw_data = load_raw_data('raw_data.csv')

    # Clean the data
    cleaned_data = clean_data(raw_data)

    # Perform initial data analysis
    initial_data_analysis(cleaned_data)

    # Save the cleaned data to a new CSV file
    cleaned_data.to_csv('cleaned_data.csv', index=False)

if __name__ == '__main__':
    main()
