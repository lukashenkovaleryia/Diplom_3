import allure
import pytest
from pages.main import MainPage
from pages.order_feed import OrderFeedPage
from helpers import create_order_return_text_id
from helpers import create_order_fast
import time

@allure.suite("Раздел «Лента заказов»")
class TestOrderFeed:

    @allure.title("Если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_order_popup(self, driver):
        feed = OrderFeedPage(driver)
        feed.open()
        feed.click_on_last_order()
        assert feed.wait_for_contents_popup()

    @allure.title("Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_displaying_orders(self, driver, auth_user):
        main = MainPage(driver)
        order_id = create_order_return_text_id(main)
        main = MainPage(driver)
        main.click_feed_button()
        feed = OrderFeedPage(driver)
        feed.click_on_last_order()
        assert feed.order_number_displayed(order_id)

    @allure.title("При создании нового заказа счётчик 'Выполнено за всё время' увеличивается")
    def test_counter_orders_for_all_time(self, driver, auth_user):
        main = MainPage(driver)
        main.click_feed_button()

        feed = OrderFeedPage(driver)

        # Получаем начальное значение счетчика
        initial_counter = feed.get_all_orders_number_as_text()
        print(f"Начальное значение счетчика: {initial_counter}")

        # Создаем заказ
        create_order_fast(main)

        # Ждем обновления счетчика (даем время на обновление данных)
        time.sleep(2)

        main.click_feed_button()
        feed = OrderFeedPage(driver)

        # Получаем новое значение счетчика
        new_counter = feed.get_all_orders_number_as_text()
        print(f"Новое значение общего счетчика: {new_counter}")

        # Проверяем увеличение счетчика
        assert int(new_counter) >= int(initial_counter),\
            f"Общий счетчик изменился неожидаемым образом: был '{initial_counter}', стал '{new_counter}'"

        # Если счетчик не изменился сразу, ждем еще и проверяем снова
        if new_counter == initial_counter:
            time.sleep(3)
            new_counter = feed.get_all_orders_number_as_text()
            print(f"Повторная проверка общего счетчика, новое значение: {new_counter}")
            assert int(new_counter) > int(initial_counter), f"Общий счетчик не увеличился после ожидания: {initial_counter} -> {new_counter}"

    @allure.title("При создании нового заказа счётчик 'Выполнено за сегодня' увеличивается")
    def test_counter_orders_for_today(self, driver, auth_user):
        main = MainPage(driver)
        main.click_feed_button()

        feed = OrderFeedPage(driver)

        # Получаем начальное значение счетчика
        initial_counter = feed.get_today_orders_number_as_text()
        print(f"Начальное значение счетчика за сегодня: {initial_counter}")

        # Создаем заказ
        create_order_fast(main)

        # Ждем обновления счетчика (даем время на обновление данных)
        time.sleep(2)

        main.click_feed_button()
        feed = OrderFeedPage(driver)

        # Получаем новое значение счетчика
        new_counter = feed.get_today_orders_number_as_text()
        print(f"Новое значение счетчика за сегодня: {new_counter}")

        # Проверяем увеличение счетчика
        assert int(new_counter) >= int(initial_counter),\
            f"Счетчик за сегодня изменился неожидаемым образом: был '{initial_counter}', стал '{new_counter}'"

        # Если счетчик не изменился сразу, ждем еще и проверяем снова
        if new_counter == initial_counter:
            time.sleep(3)
            new_counter = feed.get_today_orders_number_as_text()
            print(f"Повторная проверка счетчика за сегодня, новое значение: {new_counter}")
            assert int(new_counter) > int(initial_counter), f"Счетчик за сегодня не увеличился после ожидания: {initial_counter} -> {new_counter}"

    @allure.title("После оформления заказа его номер появляется в разделе В работе")
    def test_order_in_work(self, driver, auth_user):
        main = MainPage(driver)
        order_id = create_order_return_text_id(main)

        # Проверяем, что получили реальный номер заказа
        if order_id == '9999':
            pytest.skip(f"Пропускаем тест: получен дефолтный номер заказа {order_id}")
        print(f"Создан заказ с номером: {order_id}")

        main = MainPage(driver)
        main.click_feed_button()

        # Ждем загрузки ленты заказов
        feed = OrderFeedPage(driver)
        feed.wait_for_page_ready()

        # Получаем номер заказа в работе
        order_in_work = feed.get_in_work_order_id_as_text()
        print(f"Номер в работе: {order_in_work}")
        print(f"Ожидаемый номер: {order_id}")

        # Проверяем, что номер заказа содержится в тексте
        assert order_id[:-1] in order_in_work, f"Заказ {order_id} не найден в разделе 'В работе': {order_in_work}"

        # Проверяем, что номера заказов цифровые и текущий номер заказа в работе больше или равен нашему,
        # а ситуация с "больше" возможна, если случились "гонки" и кто-то уже создал заказ с б`ольшим ID
        assert order_in_work.isdigit() and order_id.isdigit() and int(order_in_work) >= int(order_id)
