# Selenium Web Scraper for NASDAQ Stock Screener

This Python script uses the Selenium library to automate the process of downloading data from the NASDAQ Stock Screener website. It simulates a headless Firefox browser to access the webpage, click on the "Download Data" button, and download the data.

## Prerequisites

Before running this script, ensure you have the following prerequisites:

1. **Python**: You need Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

2. **Selenium**: You must have the Selenium library installed. You can install it using pip:

   ```
   pip install selenium
   ```

3. **Mozilla Firefox**: Make sure you have Mozilla Firefox installed on your system. You can download it from the official website: [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/new/).

4. **GeckoDriver**: You also need to download the GeckoDriver, which is the Firefox WebDriver. Make sure to download the appropriate version for your Firefox installation from the [GeckoDriver releases page](https://github.com/mozilla/geckodriver/releases) and place it in your system's PATH.

## How to Use

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory containing the script.

3. Run the script using the following command:

   ```
   python downloader.py
   ```

   Replace `downloader.py` with the actual name of the script.

4. The script will launch a headless Firefox browser, navigate to the NASDAQ Stock Screener webpage, and download the data by clicking the "Download Data" button.

5. The downloaded data will be saved to your default download directory.

## Important Notes

- The script uses a headless browser (no graphical interface), which means it can run in the background without opening a visible browser window.

- Ensure that your Mozilla Firefox version and GeckoDriver version are compatible. If you encounter any issues, consider updating both Firefox and GeckoDriver.

- The script uses the NASDAQ Stock Screener website URL mentioned in the code. You can modify the URL to target a different webpage if needed.

- Depending on your internet speed and the NASDAQ website's responsiveness, you may need to adjust the waiting times (e.g., `time.sleep` and `WebDriverWait`) to ensure the page fully loads before attempting to download the data.

