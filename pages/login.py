import allure
from pages.base import BasePage
from locators.login_locators import LoginPageLocators

class LoginPage(BasePage):

    @allure.step('Вводим данные пользователя и авторизуемся')
    def login_user(self, email, password):
        self.input_text(LoginPageLocators.EMAIL_FIELD, email)
        self.input_text(LoginPageLocators.PASSWORD_FIELD, password)
        self.click_on_element(LoginPageLocators.ENTER_BUTTON)
        self.wait_invisibility(LoginPageLocators.ENTER_BUTTON)

    @allure.step('Нажимаем на Восстановить пароль')
    def click_restore_password(self):
        self.click_on_element(LoginPageLocators.RESTORE_PASSWORD)
