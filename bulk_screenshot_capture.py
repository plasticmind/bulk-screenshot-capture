import csv
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

import time
import os
from PIL import Image
from urllib.parse import quote

chrome_options = Options()
chrome_options.add_argument("--headless")  # Runs Chrome in headless mode.
service = Service(executable_path='../../chromedriver/mac-120.0.6099.71/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)
crop_height = 600  # Height in pixels to crop the screenshot

folder_path = './screenshots'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

with open('./capture_urls.csv', newline='') as csvfile:
    url_reader = csv.reader(csvfile, delimiter=',')
    for row in url_reader:
        url = row[0]

        # Ensure URL starts with http:// or https://
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'https://' + url

        # Encode URL to prevent errors
        encoded_url = quote(url, safe=":/")

        try:
            driver.get(encoded_url)
            time.sleep(2)  # Wait 2 seconds for the page to load

            # Define screenshot_path here
            screenshot_filename = url.replace('/', '_')[:100] + '.png'
            screenshot_path = os.path.join(folder_path, screenshot_filename)

            driver.save_screenshot('temp_screenshot.png')  # Save full screenshot temporarily before cropping
            img = Image.open('temp_screenshot.png')
            cropped_img = img.crop((0, 0, img.width, crop_height))  # Crop to the top 600px
            cropped_img.save(screenshot_path)  # Save the cropped image
            os.remove('temp_screenshot.png')  # Remove temporary full screenshot
        except WebDriverException as e:
            first_line_error = e.msg.split('\n')[0]  # Extract the first line of the error message
            print(f"Error capturing {url}: {first_line_error}")
    print("\033[96m\033[1mAll URLs have been processed successfully. 🏁\033[0m")