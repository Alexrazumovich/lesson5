class Store():
    def __init__(self, name,address):
        self.name = name
        self.address = address
        self.items = {}
    def add_product(self,product_name,product_price):
        self.items[product_name] = product_price
    def delete_product(self,product_name):
        a=self.items.pop(product_name)
        #print(f"delete product- {a.product_name} с ценой {a.product_price}")
    def get_product_price(self,product_name):
        return self.items.get(product_name,None)
    def set_product_price(self,product_name,price):
        self.items[product_name] = price
store1=Store('ashan1','address1')
store2=Store('ashan2','address2')
store3=Store('ashan3','address3')
store1.add_product('яблоки',80)
store1.add_product('груши',90)
store2.add_product('молоко',85)
store2.add_product('сметана',64)
store3.add_product('хлеб',30)
store3.add_product('булочка',40)
store3.delete_product('хлеб')
print(f"Цена булочки была {store3.get_product_price('булочка')}")
store3.set_product_price('булочка',50)
print(f"А теперь цена булочки будет {store3.get_product_price('булочка')}")
print(f"В магазине {store1.name} по адресу {store1.address} есть такие товары:")
for product, price in store1.items.items():
    print(f"{product} - {price}")
