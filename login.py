from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import sys, time
# import openpyxl
# import unittest
from datetime import date, datetime

Chrome_path = 'D:/ChromeDriver/chromedriver.exe'
driver = webdriver.Chrome(Chrome_path)
driver.get("https://web.whatsapp.com/")
time.sleep(2)
import xlrd
Path = "C:\\Users\\Dell\\Desktop\\NumList.xlsx"
workbook = xlrd.open_workbook(Path)
worksheet = workbook.sheet_by_name('List')
value = worksheet.cell(3, 2)


# wb = openpyxl.load_workbook(Path)
# sheet = wb.active
# print(sheet.cell(3,2).value)

search_number = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys(value)
search_number.click()

text_input = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]').send_keys("Greetings")
text_input.send_keys(Keys.RETURN)

# google_login = driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/section[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[2]")
# google_login.click()
# emailElem = driver.find_element_by_id("identifierId")
# emailElem.send_keys("asirintesar97@gmail.com")
# nextButton = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span')
# nextButton.click()
# time.sleep(1)
# passwordElem = browser.find_element_by_id('Passwd')
# passwordElem.send_keys('MyPassword')
# signinButton = browser.find_element_by_id('signIn')
# signinButton.click()
# create_task = driver.find_element_by_class_name('OnboardingButton OnboardingButton--flatTheme')
# create_task.click()

