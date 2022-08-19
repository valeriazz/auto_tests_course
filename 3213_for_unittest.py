from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestForm(unittest.TestCase):
    def test_form1(self):
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            input1 = browser.find_element(By.CLASS_NAME, "form-control.first:required")
            input1.send_keys("Пайтон1")
            input2 = browser.find_element(By.CLASS_NAME, "form-control.second:required")
            input2.send_keys("Пайтон2")
            input3 = browser.find_element(By.CLASS_NAME, "form-control.third:required")
            input3.send_keys("Пайтон3")

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()
            time.sleep(1)

            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text

            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Successful registration")

        finally:
            time.sleep(10)
            browser.quit()

    def test_form2(self):
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            input1 = browser.find_element(By.CLASS_NAME, "form-control.first:required")
            input1.send_keys("Пайтон1")
            input2 = browser.find_element(By.CLASS_NAME, "form-control.second:required")
            input2.send_keys("Пайтон2")
            input3 = browser.find_element(By.CLASS_NAME, "form-control.third:required")
            input3.send_keys("Пайтон3")

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()
            time.sleep(1)

            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text

            self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                             "Successful registration")

        finally:
            time.sleep(10)
            browser.quit()


if __name__ == "__main__":
    unittest.main()



