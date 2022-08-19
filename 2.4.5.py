from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(13)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    #price = browser.find_element(By.ID, "price")
    #element = price.text
    button = browser.find_element(By.ID, "book")
    button_click = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button.click()

    num = browser.find_element(By.ID, "input_value")
    x = num.text
    y = calc(x)

    button2 = browser.find_element(By.ID, "answer")
    button2.send_keys(y)

    button3 = browser.find_element(By.ID, "solve")
    button3.click()
    time.sleep(5)

finally:
    time.sleep(10)
    browser.quit()