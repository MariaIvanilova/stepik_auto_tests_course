from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestSite(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        self.browser.quit()

        
    def test_site(self):
        link = "http://suninjuly.github.io/registration1.html"
        # link = "http://suninjuly.github.io/registration2.html"
        self.browser.get(link)

        # Ваш код, который заполняет обязательные поля
        self.input1 = self.browser.find_element(By.CSS_SELECTOR, 'div.first_block input.form-control.first')
        self.input1.send_keys("Ivan")
        self.input2 = self.browser.find_element(By.CSS_SELECTOR, 'div.first_block input.form-control.second')
        self.input2.send_keys("Petrov")
        self.input3 = self.browser.find_element(By.CSS_SELECTOR, 'div.first_block input.form-control.third')
        self.input3.send_keys("Email@mail.com")

        # Отправляем заполненную форму
        self. button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        self.button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        self.welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        self.welcome_text = self.welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        # assert "Congratulations! You have successfully registered!" == welcome_text
        self.assertEqual("Congratulations! You have successfully registered!", self.welcome_text, "Registration failed")

    def test_site2(self):
        # link = "http://suninjuly.github.io/registration1.html"
        link = "http://suninjuly.github.io/registration2.html"
        self.browser.get(link)

        # Ваш код, который заполняет обязательные поля
        self.input1 = self.browser.find_element(By.CSS_SELECTOR, 'div.first_block input.form-control.first')
        self.input1.send_keys("Ivan")
        self.input2 = self.browser.find_element(By.CSS_SELECTOR, 'div.first_block input.form-control.second')
        self.input2.send_keys("Petrov")
        self.input3 = self.browser.find_element(By.CSS_SELECTOR, 'div.first_block input.form-control.third')
        self.input3.send_keys("Email@mail.com")

        # Отправляем заполненную форму
        self. button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        self.button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        self.welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        self.welcome_text = self.welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        # assert "Congratulations! You have successfully registered!" == welcome_text
        self.assertEqual("Congratulations! You have successfully registered!", self.welcome_text, "Registration failed")
        
if __name__ == "__main__":
    unittest.main()

