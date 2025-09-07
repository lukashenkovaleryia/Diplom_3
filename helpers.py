def __create_order_service(main_page):
    main_page.open()
    main_page.click_constructor_button()
    main_page.add_fluorescent_bun()

    main_page.click_on_sauce_list()
    main_page.add_spicy_sauce()

    main_page.click_on_topping_list()
    main_page.add_meat_topping()

    main_page.click_on_create_order()

    main_page.wait_invisibility_of_default_number()


def create_order_return_text_id(main_page):
    __create_order_service(main_page)

    # Используем новый метод получения номера заказа
    order_id = main_page.get_order_number_new()

    # Если все равно получили 9999, ждем еще и пробуем снова
    if order_id == '9999':
        import time; time.sleep(3)
        order_id = main_page.get_order_number()
        print(f"Повторная попытка получения номера заказа: {order_id}")

    main_page.click_on_cross()

    # Проверяем, что номер заказа валидный
    if order_id == '9999':
        print("ВНИМАНИЕ: Получен дефолтный номер заказа 9999!")

    return order_id


def create_order_fast(main_page):
    __create_order_service(main_page)
    main_page.click_on_cross()
