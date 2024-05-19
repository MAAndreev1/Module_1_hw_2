name = input('Наименование товара >>> ')
price = int(input('Цена товара >>> '))
weight = int(input('Вес товара >>> '))
money = int(input('Количество денег от покупателя >>> '))

money_refund = money - price * weight

print()
print(f'Чек {name} - {weight}кг - {price}руб/кг Итог: {price * weight}руб Внесено: {money}руб Сдача {money_refund}руб')