import pandas as pd

def clean_csv():
    # Prompt user for the file name
    file_path = input("Enter the name of the CSV file: ")

    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)

        # Check if the expected headers are present
        expected_headers = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']
        if not all(header in df.columns for header in expected_headers):
            raise ValueError("The file does not have the expected headers.")

        # Display basic information about the DataFrame
        print("\nOriginal Data:")
        print(df.info())

        # Drop rows with missing values
        df = df.dropna()

        # Convert 'Date' column to datetime format
        df['Date'] = pd.to_datetime(df['Date'])

        # Display updated information about the DataFrame
        print("\nCleaned Data:")
        print(df.info())

        # Save the cleaned DataFrame back to a CSV file
        cleaned_file_path = file_path.replace(".csv", "_cleaned.csv")
        df.to_csv(cleaned_file_path, index=False)

        print(f"\nCleaned data saved to: {cleaned_file_path}")

    except FileNotFoundError:
        print(f"File '{file_path}' not found. Please check the file path and try again.")
    except pd.errors.EmptyDataError:
        print(f"The file '{file_path}' is empty.")
    except ValueError as ve:
        print(str(ve))

# Call the function to clean the CSV file
clean_csv()
