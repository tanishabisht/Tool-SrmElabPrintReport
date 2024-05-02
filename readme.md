# Tool - SRM Elab DAA Report Downloader

This Python script automates the process of downloading reports for the DAA Lab at SRM University. All reports will be saved in the specified Downloads folder.

## Instructions to run the tool
To use this script, follow these instructions:
1. **Fork and Clone the Repository**: Begin by forking the repository and then clone it to your local machine.
2. **Configure the Script**: Open the `script.py` file and set the following variables with your specific details:
   ```python
   PATH = '<exact path where your Chrome driver is downloaded>'
   TIME = 3  # Wait time for page loads and downloads
   USERNAME = '<SRM roll number e.g. RA1911003010xxx>'
   PASSWORD = '<password for your elab>'
   DOWNLOAD_FOLDER = '<exact path where you want your files to be downloaded>'
   ```

## Dependencies used
To run the script, you need to install and configure several components:
1. **Selenium**:
   Install Selenium via pip:
   ```bash
   pip install selenium
   ```
2. **Chrome WebDriver**:
   Download the Chrome WebDriver from [Chromium.org](https://sites.google.com/a/chromium.org/chromedriver/downloads).

3. **Environment Configuration**:
   After downloading, add the path to the Chrome WebDriver to your system's environment variables. For guidance on setting up the driver on Windows, refer to [this guide on Stack Overflow](https://stackoverflow.com/questions/42524114/how-to-install-geckodriver-on-a-windows-system).