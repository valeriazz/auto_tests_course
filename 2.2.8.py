import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Иннокентий")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Кощеевич")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("k@tut.ru")

    #with open("test.txt", "w") as file:
    #content = file.write("automationbypython")  # create test.txt file

    current_dir = os.path.abspath(os.path.dirname("2.2.8.py"))
    file_name = "file.txt"
    file_path = os.path.join(current_dir, file_name)

    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(2)


finally:
    time.sleep(10)
    browser.quit()