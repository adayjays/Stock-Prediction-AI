import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

class StockPricePredictor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        self.scaler = MinMaxScaler(feature_range=(0, 1))
        self.model = None

    def load_data(self):
        self.data = pd.read_csv(self.file_path)

    def preprocess_data(self):
        training_data = self.data['Open'].values.reshape(-1, 1)
        self.training_data_normalized = self.scaler.fit_transform(training_data)

    def create_sequences(self):
        X_train, y_train = [], []
        for i in range(60, len(self.training_data_normalized)):
            X_train.append(self.training_data_normalized[i-60:i, 0])
            y_train.append(self.training_data_normalized[i, 0])
        self.X_train, self.y_train = np.array(X_train), np.array(y_train)
        self.X_train = np.reshape(self.X_train, (self.X_train.shape[0], self.X_train.shape[1], 1))

    def build_model(self):
        self.model = Sequential()
        self.model.add(LSTM(units=50, return_sequences=True, input_shape=(self.X_train.shape[1], 1)))
        self.model.add(LSTM(units=50, return_sequences=True))
        self.model.add(LSTM(units=50))
        self.model.add(Dense(units=1))
        self.model.compile(optimizer='adam', loss='mean_squared_error')

    def train_model(self, epochs=10, batch_size=32):
        self.model.fit(self.X_train, self.y_train, epochs=epochs, batch_size=batch_size)

    def prepare_test_data(self):
        test_data = self.data[self.data['Date'] >= '2017-01-01']['Open'].values.reshape(-1, 1)
        self.actual_prices = test_data.flatten()

        total_data = pd.concat((self.data['Open'], self.data['Open'][len(self.data)-len(test_data):]), axis=0)
        inputs = total_data.iloc[len(total_data) - len(test_data) - 60:].values
        inputs = inputs.reshape(-1, 1)
        self.inputs = self.scaler.transform(inputs)

        X_test = []
        for i in range(60, len(self.inputs)):
            X_test.append(self.inputs[i-60:i, 0])
        self.X_test = np.array(X_test)
        self.X_test = np.reshape(self.X_test, (self.X_test.shape[0], self.X_test.shape[1], 1))

    def predict_prices(self):
        predicted_prices = self.model.predict(self.X_test)
        self.predicted_prices = self.scaler.inverse_transform(predicted_prices)

    def plot_results(self):
        plt.figure(figsize=(16, 8))
        plt.plot(self.actual_prices, color='blue', label='Actual Prices')
        plt.plot(self.predicted_prices, color='red', label='Predicted Prices')
        plt.title('Google Stock Price Prediction')
        plt.xlabel('Time')
        plt.ylabel('Stock Price')
        plt.legend()
        plt.show()

def main():
    # Instantiate the StockPricePredictor
    predictor = StockPricePredictor("google_stock_data.csv") 

    # Load and preprocess the data
    predictor.load_data()
    predictor.preprocess_data()

    # Create sequences for training
    predictor.create_sequences()

    # Build and train the LSTM model
    predictor.build_model()
    predictor.train_model()

    # Prepare test data and predict prices
    predictor.prepare_test_data()
    predictor.predict_prices()

    # Plot the results
    predictor.plot_results()

if __name__ == "__main__":
    main()
