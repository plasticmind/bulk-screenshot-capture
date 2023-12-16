# Bulk Screenshot Capture

Capture screenshots of web pages specified in a CSV file.

This script uses Python, Selenium, and the Chrome WebDriver to capture screenshots of web pages from CSV file containing URLs. The script visits each URL, captures a screenshot, and saves it to a folder.

The script saves the screenshots as PNG files in a specified folder.The screenshots are cropped to the top 600 pixels of the web page. This can be adjusted by changing the `crop_height` variable at the top of the script.

## Dependencies

- Selenium
- Chrome WebDriver
- Pillow

## Usage

### Install the required dependencies.

```
pip install selenium
pip install pillow
```

Download and install the Chrome WebDriver from https://googlechromelabs.github.io/chrome-for-testing/. 

Make sure to download the version that matches the version of Chrome installed on your system, or you won't be able to run the script. If you don't, you'll get an error that looks something like:

```
This version of ChromeDriver only supports Chrome version 118
Current browser version is 120.0.6099.109 with binary path /Applications/Google Chrome.app/Contents/MacOS/Google Chrome
```

This message means that the ChromeDriver version you downloaded only supports Chrome version 118, but you have Chrome version 120 installed.

### Set the path to the Chrome WebDriver executable in the `service` variable.

For example:

```
service = webdriver.Chrome('../../chromedriver/mac-118.0.5993.70/chromedriver-mac-x64/chromedriver')
```

In this example, the 118.x Chrome WebDriver executable for the Mac (ARM) is located in the `../../` which is two directories up from the current directory. Adjust the path to match the location of the relevant Chrome WebDriver executable for your system and browser.

### Update the CSV with the URLs you want to capture. 
   
Each row in the CSV file should contain a single URL.

### Set the folder path where the screenshots should be saved in the `folder_path` variable. (Optional)

This is set to `screenshots` by default. You can leave it as is, or change it to a different folder path.

### Run the script.

Run the script using the following command:

```
python bulk_screenshot_capture.py
```

If you're running python3, you may need to use `python3` instead of `python`.

The script requires Chrome WebDriver to be installed and the path to the executable to be provided.

The script will read the CSV file, visit each URL, capture a screenshot, and save it to the specified folder. If an error occurs while capturing a screenshot, the script prints an error message to the console.

## Issues

If you encounter any issues, please [report them here](https://github.com/plasticmind/bulk-screenshot-capture/issues).