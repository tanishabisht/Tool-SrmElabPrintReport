from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import shutil




# Initialize variables
PATH = '<exact path where your chrome driver is downloaded>'
TIME = 3
USERNAME = '<SRM roll number e.g. RA1911003010xxx>'
PASSWORD = '<password of your elab>'
DOWNLOAD_FOLDER = '<exact path where you want your files to be downloaded>'




options = webdriver.ChromeOptions()
preferences = {'download.default_directory': DOWNLOAD_FOLDER}
options.add_experimental_option('prefs', preferences)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options, executable_path=PATH)




driver.get('https://care.srmist.edu.in/srmktrada/login')
print(driver.title)




# LOGGING IN
[username,password] = driver.find_elements_by_class_name("mat-input-element")
username.send_keys(USERNAME)
password.send_keys(PASSWORD)
password.send_keys(Keys.RETURN)
time.sleep(TIME)




# SELECTING DAA
daa = driver.find_element_by_xpath('/html/body/app-root/div/app-student-home/div/mat-card/div/div/app-student-home-card/mat-card')
daa.click()
time.sleep(TIME)




# LOOPING OVER THE CIRCLE OF QUESTIONS
skipped = 0
for i in range(100):
    
    # Open the question
    if i == 0:
        #Select 1st question
        question = driver.find_element_by_css_selector('#svgChart g:nth-child(2) g:nth-child(4) path:nth-child(100)')
        question.click()
        time.sleep(TIME)
    else:
        next = driver.find_element_by_css_selector('button.mat-raised-button:nth-child(3)')
        next.click()
        time.sleep(TIME)

    #Switch to cpp
    lan = driver.find_element_by_xpath('/html/body/app-root/div/app-student-solve/div[2]/app-solve-question/div/div[1]/mat-form-field/div/div[1]/div')
    lan.click()
    time.sleep(TIME)
    cpp = driver.find_element_by_css_selector('#mat-option-1 span:nth-child(1)')
    cpp.click()
    time.sleep(TIME)

    #Evaluate
    evaluate = driver.find_element_by_xpath('/html/body/app-root/div/app-student-solve/div[2]/app-solve-question/div/div[2]/div[2]/mat-card/div[3]/button[2]')
    evaluate.click()
    time.sleep(TIME)

    # Result
    result = 'null'
    try:
        result = driver.find_element_by_link_text("RESULT - 100%")
    except:
        print("Skipping Question",i+1)
        skipped = skipped + 1
    
    if result!='null':
        print('value of i  ::  ', i)
        while len(os.listdir(DOWNLOAD_FOLDER))!=i-skipped+1:
            print('noOfFiles : i-skipped  ::  ', len(os.listdir(DOWNLOAD_FOLDER)), ' : ', i-skipped+1)
            download = driver.find_element_by_xpath('/html/body/app-root/div/app-student-solve/div[2]/app-solve-question/div/div[2]/div[2]/mat-card/div[4]/a[2]')
            download.click()
            time.sleep(TIME)
            if(len(os.listdir(DOWNLOAD_FOLDER))==i-skipped+1):
                filename = max([DOWNLOAD_FOLDER + "\\" + f for f in os.listdir(DOWNLOAD_FOLDER)], key=os.path.getctime)
                shutil.move(filename, os.path.join(DOWNLOAD_FOLDER,'report'+str(i)+'.png'))
                time.sleep(TIME+2)




driver.quit()