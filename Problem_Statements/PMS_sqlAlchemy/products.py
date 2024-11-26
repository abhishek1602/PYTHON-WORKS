class Product:

    def __init__(self, product_id, product_name, product_price):
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = float(product_price)

    def __repr__(self):
        return f"Product('{self.product_id}', '{self.product_name}', {self.product_price})"


        