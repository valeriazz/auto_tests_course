import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

def answer():
    return math.log(int(time.time()))

@pytest.mark.parametrize('link',
                         ["https://stepik.org/lesson/236895/step/1",
                        "https://stepik.org/lesson/236896/step/1",
                        "https://stepik.org/lesson/236897/step/1",
                        "https://stepik.org/lesson/236898/step/1",
                        "https://stepik.org/lesson/236899/step/1",
                        "https://stepik.org/lesson/236903/step/1",
                        "https://stepik.org/lesson/236904/step/1",
                        "https://stepik.org/lesson/236905/step/1"])
class TestMessage:
    def test_answer_is_correct(self, browser, link):
        browser.get(link)
        browser.implicitly_wait(10)
        input1 = browser.find_element(By.TAG_NAME, "textarea")
        input1.send_keys(str(answer()))
        button = browser.find_element(By.CLASS_NAME, "submit-submission")
        button.click()
        message = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
        message_needed = message.text

        assert "Correct!" == message_needed, 'текст в опциональном фидбеке НЕ совпадает!'

if __name__ == "__main__":
    pytest.main()