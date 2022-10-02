import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.swagbucks.com/surveys?lang=nl")

mail= "Fill in mail"
passw="Fill in pass"

searchmail= driver.find_element(By.ID, "sbxJxRegEmail")
searchpass= driver.find_element(By.ID, "sbxJxRegPswd")
searchbut= driver.find_element(By.ID, "loginBtn")

searchmail.send_keys(mail)
searchpass.send_keys(passw)
searchbut.send_keys(Keys.RETURN)

try:
    while 1==1:
        searchOption = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "surveyQuestionAnswers"))
        )

        searchOption.click()
        time.sleep(0.5)

        searchChoise = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[@data-index= 0]"))
        )

        searchChoise.click()
        time.sleep(0.5)

        searchSubmit = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@type='button'][@class='surveyDashboardCTA sbCta sbBgPrimaryColor']"))


        )

        searchSubmit.click()

        time.sleep(0.5)

except:
    time.sleep(3)





