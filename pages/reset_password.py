import allure
from pages.base import BasePage
from locators.reset_password_locators import ResetPasswordLocators
import fakers


class ResetPasswordPage(BasePage):

    @allure.step('Вводим почту')
    def input_email(self):
        self.input_text(ResetPasswordLocators.EMAIL_FIELD, fakers.generated_email())

    @allure.step('Нажимаем Восстановить')
    def click_restore_button(self):
        self.click_on_element(ResetPasswordLocators.RESTORE_PASSWORD_BUTTON)
        self.wait_for_element(ResetPasswordLocators.SAVE_PASSWORD_BUTTON)

    @allure.step('Нажимаем на показать пароль')
    def click_show_password_button(self):
        self.click_on_element(ResetPasswordLocators.SAVE_PASSWORD_BUTTON)

    @allure.step('Проверяем активность поля Пароль')
    def check_active_field(self):
        return self.find_element_with_visibility_wait(ResetPasswordLocators.SHOW_PASSWORD_BUTTON)
