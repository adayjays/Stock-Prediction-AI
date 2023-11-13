# Stock Price Predictor

### data_cleaner.py

**Data Cleaner**

This script, `data_cleaner.py`, is designed to clean CSV files with specific headers: Date, Open, High, Low, Close, Volume, Adj Close. It utilizes the pandas library to handle data cleaning tasks such as handling missing values, converting data types, and ensuring the presence of expected headers.

#### Usage

1. **Run the Script**

   ```bash
   python data_cleaner.py
   ```

2. **Enter File Name**

   - The script will prompt you to enter the name of the CSV file you want to clean.

3. **Check the Cleaned Data**

   - The script will display information about the original and cleaned data.
   - The cleaned data will be saved to a new CSV file with "_cleaned" appended to the original file name.

#### Requirements

Ensure you have the required libraries installed by running:

```bash
pip install -r requirements.txt
```

### main.py

**Stock Price Prediction with LSTM**

This script, `main.py`, demonstrates stock price prediction using a Long Short Term Memory (LSTM) network. It follows a step-by-step process, including loading the dataset, normalizing data, creating data structures, building and training the LSTM model, and making predictions.

#### Usage

1. **Run the Script**

   ```bash
   python main.py
   ```

2. **Input File Name**

   - The script will prompt you to input the name of the CSV file containing historical stock data.

3. **Check Predictions**

   - The script will display the actual and predicted stock prices, providing a visual representation of the model's performance.

   ![Predicted Data](/output/Figure_1.png)


#### Requirements

Ensure you have the required libraries installed by running:

```bash
pip install -r requirements.txt
```

