import pandas as pd

# Load the processed data
data = pd.read_csv('cleaned_data.csv')

# Remove non-numeric characters and convert columns to the appropriate data types
data['Last Sale'] = data['Last Sale'].str.replace('$', '').astype(float)
data['Net Change'] = data['Net Change'].astype(float)
data['% Change'] = data['% Change'].str.replace('%', '').astype(float)

# Now the data should be in a format suitable for machine learning

data.to_csv('processed_data.csv', index=False)