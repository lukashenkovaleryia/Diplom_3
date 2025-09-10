import pytest
from locators.main_locators import MainPageLocators
from data import TestData
import allure
from pages.main import MainPage
from helpers import create_order_return_text_id


@allure.suite("Основной функционал (Main)")
class TestMain:

    @allure.title("Переходим на главную страницу")
    def test_open_main_page_constructor_button(self, driver):
        main = MainPage(driver)
        main.open()
        main.wait_for_page_ready()
        main.click_constructor_button()
        assert main.ingredient_found()

    @allure.title("Переходим на Ленту заказов")
    def test_open_feed_page_check_ready_orders(self, driver):
        main = MainPage(driver)
        main.open()
        main.click_feed_button()
        assert main.find_element_with_visibility_wait(MainPageLocators.ORDER_LIST_READY)

    @allure.title("Открываем ингредиент кликом")
    @pytest.mark.parametrize("ingredients", TestData.INGREDIENTS)
    def test_click_one_ingredient(self, driver, ingredients):
        main = MainPage(driver)
        main.open()
        ingredient_locator = MainPageLocators.by_ingredient_name(ingredients)
        main.click_on_element(ingredient_locator)
        assert main.ingredient_details_found()

    @allure.title("Закрываем ингредиент кликом на крестик")
    @pytest.mark.parametrize("ingredients", TestData.INGREDIENTS)
    def test_click_one_ingredient_and_close(self, driver, ingredients):
        main = MainPage(driver)
        main.open()
        ingredient_locator = MainPageLocators.by_ingredient_name(ingredients)
        main.click_on_element(ingredient_locator)
        main.click_on_cross()
        assert main.close_button_invisible()

    @allure.title("Увеличиваем счетчик ингредиента при его добавлении в заказ")
    def test_ingredient_counter(self, driver):
        main = MainPage(driver)
        main.open()
        main.click_constructor_button()
        main.add_fluorescent_bun()
        assert int(main.ingredient_count_number()) == 2

    @allure.title("Оформляем заказ авторизованным пользователем")
    def test_create_order_after_login_user(self, driver, auth_user):
        main = MainPage(driver)
        order_id = create_order_return_text_id(main)
        main.close_button_invisible()
        assert order_id is not None and order_id and int(order_id) > 0
