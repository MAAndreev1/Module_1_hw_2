price = int(input('Цена товара >>>'))
weight = int(input('Вес товара >>>'))
money = int(input('Количество денег от покупателя >>>'))

print(f'Сдача составила {money - price * weight}')