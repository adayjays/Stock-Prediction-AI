# Import necessary modules from Selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

try:
    # Configure Firefox options for a headless (invisible) browser
    fireFoxOptions = Options()
    fireFoxOptions.add_argument("--headless")

    # Initialize a Firefox WebDriver with the specified options
    browser = webdriver.Firefox(options=fireFoxOptions)

    # Navigate to the NASDAQ Stock Screener webpage
    browser.get('https://www.nasdaq.com/market-activity/stocks/screener')

    # Find and select the "Download Data" button using a CSS selector
    button = browser.find_element(By.CSS_SELECTOR, ".ns-download-1")

    # Simulate a click action on the "Download Data" button
    ActionChains(browser).click(button)

    # Wait for 5 seconds (adjust as needed) to allow the download to start
    time.sleep(5)

    # Retrieve the name of the downloaded file from the "download" attribute of the button
    fileName = button.get_attribute("download")

    # Click the "Download Data" button again to confirm the download (if needed)
    browser.find_element(By.CSS_SELECTOR, ".ns-download-1").click()

    # Wait until the webpage's document state is "complete" before proceeding
    WebDriverWait(browser, 60).until(lambda d: d.execute_script("return document.readyState") == "complete")

finally:
    try:
        # Close the browser window, regardless of whether the script succeeded or failed
        browser.close()
    except:
        pass
