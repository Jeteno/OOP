import numpy as np

class Product():
   default_name = 'Apple'
   default_price = 20

   @staticmethod
   def default_info():
      print(f'Название: {Product.default_name}')
      print(f'Цена: {Product.default_price}')

   def __init__(self, name, price, variety):
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

   def info(self):
      print(f'Название продукта: {self.name}')
      print(f'Цена продукта: {self.price}')
      print(f'Сорт продукта: {self.__variety}')
      print(f'Количество продукта в каждой поставке: {self.__quantity}')
      print(f'Всего продукта: {self.total}')

class Fruit(Product):
   def __init__(self, name, price, variety, date, view):
      super().__init__(name, price, variety)
      self.expiration_date = date
      self.classification = view

   def info(self):
      super().info()
      print(f'Срок годности: {self.expiration_date}')
      print(f'Классификация: {self.classification}')

class Order():
   def __init__(self, Fruit):
      self.price = Fruit.price
      self.quantity = Fruit.total

   def cost_calculation(self):
      self.final_cost = self.price * self.quantity
      print(f'Итого за все поставки: {self.final_cost}')

   def __gt__(self, other):
      if self.final_cost > other.final_cost:
         reuslt = 'У первого заказа стоимость больше'
      elif self.final_cost == other.final_cost:
         reuslt = 'У обоих заказов стоимость одинаковая'
      else:
         reuslt = 'У второго заказа стоимость больше'

      return reuslt

grape = Fruit('Виноград', 30, 'Киш-Миш', '3 дня', 'Ягоды')
grape.quantity_in_deliveries()
grape.info()
delivery_1 = Order(grape)
delivery_1.cost_calculation()
orange = Fruit('Апельсин', 25, 'Навел', '4 дня', 'Цитрусовые')
orange.quantity_in_deliveries()
orange.info()
delivery_2 = Order(orange)
delivery_2.cost_calculation()
print(delivery_1>delivery_2)