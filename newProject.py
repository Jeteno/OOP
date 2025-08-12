import numpy as np

class Product():
   default_name = 'Apple'
   default_price = 20

   @staticmethod
   def default_info():
      print(f'Название: {Product.default_name}')
      print(f'Цена: {Product.default_price}')

   def __init__(self, name, price, variety,):
      self.name = name
      self.price = price
      self.__variety= variety

   def quantity_in_deliveries(self):
      self.__quantity = []
      deliveries = 4

      for i in range(deliveries):
         print(f'Введите количесвто полученного товара в поставке №{i + 1}')
         amount_received = int(input())
         self.__quantity.append(amount_received)
      self.total = np.sum(self.__quantity)
      print(f'Итого в каждой поставке привозили: {self.__quantity}')

   def info(self):
      print(f'Название продукта: {self.name}')
      print(f'Цена продукта: {self.price}')
      print(f'Сорт продукта: {self.__variety}')
      print(f'Количество продукта в каждой поставке: {self.__quantity}')
      print(f'Всего продукта: {self.total}')

orange = Product('Orange', 25, 'Navel')

Product.default_info()

orange.quantity_in_deliveries()

orange.info()
