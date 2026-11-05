# Абрамовская Оксана Васильевна, 49-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request
import data

# Функция создания заказа и получения его трека
def track_order():

    # Копируется словарь с телом запроса из файла data
    order_body = data.order_body.copy()
    
    # В переменную order_response сохраняется результат запроса на создание заказа
    order_response = sender_stand_request.post_new_order(order_body)

    # Возврат трека заказа
    return order_response.json()["track"]

# Функция для позитивной проверки
def positive_assert(track):
        
    # В переменную response сохраняется результат запроса на получение заказа
    response = sender_stand_request.get_order(track)
    
    # Проверяется, что код ответа равен 200
    assert response.status_code == 200
 

# Тест 1. Успешное получение данных о заказе по его номеру (track)
def test_get_order_by_track():
    track = track_order()
    positive_assert(track)