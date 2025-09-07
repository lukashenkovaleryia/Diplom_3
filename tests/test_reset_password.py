import allure
from pages.main import MainPage
from pages.login import LoginPage
from pages.reset_password import ResetPasswordPage


@allure.suite("Восстановление пароля")
class TestResetPassword:

    @allure.title("Переходим на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_go_to_the_password_reset_page(self, driver):
        main = MainPage(driver)
        main.open()
        main.click_enter_account_button()

        login = LoginPage(driver)
        login.click_restore_password()

        assert login.get_page_url().endswith('forgot-password')

    @allure.title("Вводим email и кликаем по кнопке «Восстановить»")
    def test_input_email_and_click_reset(self, driver):
        main = MainPage(driver)
        main.open()
        main.click_enter_account_button()

        login = LoginPage(driver)
        login.click_restore_password()

        reset = ResetPasswordPage(driver)
        reset.input_email()
        reset.click_restore_button()

        assert reset.get_page_url().endswith('reset-password')

    @allure.title("Кликаем по кнопке показать/скрыть пароль и поле становится активным")
    def test_active_password_field(self, driver):

        main = MainPage(driver)
        main.open()
        main.click_enter_account_button()

        login = LoginPage(driver)
        login.click_restore_password()

        reset = ResetPasswordPage(driver)
        reset.input_email()
        reset.click_restore_button()
        reset.click_show_password_button()

        assert reset.check_active_field()
