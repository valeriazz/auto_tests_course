import os
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

current_dir = os.path.abspath(os.path.dirname("2.2.7.py"))
file_name = "file.txt"
file_path = os.path.join(current_dir, file_name)

element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys(file_path)