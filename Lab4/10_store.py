#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого вида товара на складе:
# СТОЛ ЦЕНА
print('Стол')
table_code1 = goods['Стол']
table_item1 = store[table_code1][0]
table_quantity1 = table_item1['quantity']
table_price1 = table_item1['price']
table_cost1 = table_quantity1 * table_price1
print(table_price1)

table_code = goods['Стол']
table_item = store[table_code][1]
table_quantity = table_item['quantity']
table_price = table_item['price']
table_cost = table_quantity * table_price
print(table_price)
# Cтул ЦЕНА
print('Стул')

chair_code1 = goods['Стул']
chair_item1 = store[chair_code1][0]
chair_quantity1 = chair_item1['quantity']
chair_price1 = chair_item1['price']
chair_cost1 = chair_quantity1 * chair_price1
print(chair_price1)

chair_code = goods['Стул']
chair_item = store[chair_code][2]
chair_quantity = chair_item['quantity']
chair_price = chair_item['price']
chair_cost = chair_quantity * chair_price
print(chair_price)

chair_code2 = goods['Стул']
chair_item2 = store[chair_code2][1]
chair_quantity2 = chair_item2['quantity']
chair_price2 = chair_item2['price']
chair_cost2 = chair_quantity2 * chair_price2
print(chair_price2)
# ДИВАН ЦЕНА
print('Диван')

sofa_code1 = goods['Диван']
sofa_item1 = store[sofa_code1][0]
sofa_quantity1 = sofa_item1['quantity']
sofa_price1 = sofa_item1['price']
sofa_cost1 = sofa_quantity1 * sofa_price1
print(sofa_price1)

sofa_code = goods['Диван']
sofa_item = store[sofa_code][1]
sofa_quantity = sofa_item['quantity']
sofa_price = sofa_item['price']
sofa_cost = sofa_quantity * sofa_price
print(sofa_price)
# один раз распечать сколько всего столов и их общая стоимость,
print('Стол - ', table_quantity + table_quantity1, 'шт', 'стоимость', table_cost + table_cost1, 'руб' )
# один раз распечать сколько всего стульев и их общая стоимость,
print('Стул- ', chair_quantity + chair_quantity1 + chair_quantity2, 'шт', 'стоимость', chair_cost + chair_cost1 + chair_cost2, 'руб' )
#   и т.д. на складе
print('Диван - ', sofa_quantity + sofa_quantity1, 'шт', 'стоимость', sofa_cost + sofa_cost1, 'руб' )
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

# TODO здесь ваш код
