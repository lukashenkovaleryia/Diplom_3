import allure
from pages.base import BasePage
from data import Urls
from locators.order_feed_locators import OrderFeedLocators
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class OrderFeedPage(BasePage):

    @allure.step('Перейти на страницу заказов')
    def open(self):
        self.open_page(Urls.FEED_URL)

    @allure.step('Нажать на последний созданный заказ')
    def click_on_last_order(self):
        try:  # Обычный клик
            self.click_on_element(OrderFeedLocators.LAST_ORDER)
        except ElementClickInterceptedException:
            # Если перехвачен, используем JavaScript клик
            element = self.driver.find_element(*OrderFeedLocators.LAST_ORDER)
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Проверить появление всплывающего окна с деталями заказа')
    def wait_for_contents_popup(self):
        return self.find_element_with_visibility_wait(OrderFeedLocators.ORDER_CONTENT)

    @allure.step('Проверить отображение заказа пользователя')
    def order_number_displayed(self, order_id, timeout=15):
        try:
            order_locator = OrderFeedLocators.by_order_id(order_id)
            # Ждем появления номера заказа в модальном окне
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(order_locator)
            )
        except TimeoutException:
            try:  # Если не нашли, проверяем, может быть модальное окно не открылось
                if self.wait_for_contents_popup():  # Проверяем, открыто ли модальное окно с деталями
                    # Пробуем найти номер в модальном окне с другими локаторами, содержащими order_id
                    order_number_xpath = f"//*[contains(text(), '#0{order_id}') or contains(text(), '#{order_id}')]"
                    return WebDriverWait(self.driver, 5).until(
                        EC.visibility_of_element_located((By.XPATH, order_number_xpath))
                    )
            except Exception as exception:
                print(f"Не удалось найти заказ {order_id}: {exception}")
                return False
        return False

    @allure.step('Получить число выполненных заказов за всё время')
    def get_all_orders_number_as_text(self):
        return self.get_text(OrderFeedLocators.ORDERS_FOR_ALL_TIME)

    @allure.step('Получить число выполненных заказов за сегодня')
    def get_today_orders_number_as_text(self):
        return self.get_text(OrderFeedLocators.ORDERS_FOR_TODAY)

    @allure.step('Получить номер заказа, который в работе')
    def get_in_work_order_id_as_text(self):
        return self.get_text(OrderFeedLocators.IN_WORK)
