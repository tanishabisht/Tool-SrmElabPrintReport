# SRM Elab DAA : Print Report
A python script to download reports for the DAA Lab
NOTE : All your reports will be downloaded in the DownLoads folder

## Dependancies
1. Selenium : Can be installed using the command "pip install Selenium"
2. Download Chrome geckodriver using this [link](https://sites.google.com/a/chromium.org/chromedriver/downloads)
3. Save the path where you downloaded the geckodriver in the environment variables
4. You can refer [this](https://stackoverflow.com/questions/42524114/how-to-install-geckodriver-on-a-windows-system) for installing geckodriver on a windows system.

## Instructions to Run
1. Fork then clone the repository
2. In the `script.py` initialize the variables
```
PATH = '<exact path where your chrome driver is downloaded>'
TIME = 3
USERNAME = '<SRM roll number e.g. RA1911003010xxx>'
PASSWORD = '<password of your elab>'
DOWNLOAD_FOLDER = '<exact path where you want your files to be downloaded>'
```