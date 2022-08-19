#модальные окна
#alert = browser.switch_to.alert
#alert.accept()
#alert_text = alert.text

#confirm = browser.switch_to.alert
#confirm.accept()
#confirm.dismiss()

#prompt = browser.switch_to.alert
#prompt.send_keys("My answer")
#prompt.accept()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

try:
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    num = browser.find_element(By.ID, "input_value")
    x = num.text
    y = calc(x)

    button2 = browser.find_element(By.ID, "answer")
    button2.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(2)

finally:
    time.sleep(5)
    browser.quit()