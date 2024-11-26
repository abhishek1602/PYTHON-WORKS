from products import Product
from db import sessionlocal, Product
from sqlalchemy.orm import session

class Logic:

    def __init__(self):
        self.db = sessionlocal()

    
    def add_product(self, newproduct):
        product = Product(
            product_id = newproduct.product_id,
            product_name = newproduct.product_name,
            product_price = float(newproduct.product_price),
        )
        try:
            self.db.add(product)
            self.db.commit()
            self.db.refresh(product)
            return True
        except:
            self.db.rollback()
            return False
        

    def update_product(self, product_id, newproduct_name, newproduct_price):
        product = self.db.query(Product).filter(Product.product_id == product_id).first()
        if product:
            product.product_name = newproduct_name
            product.product_price = float(newproduct_price)
            self.db.commit()

            return f"Product {product_id} Updated, Name: {newproduct_name}, Price: {newproduct_price}"
        return f"Product {product_id} Not Found"
    

    def view_update(self):
        products = self.db.query(Product).all()
        return products
    

    def apply_discount(self, discount_percentage):
        products = self.db.query(Product).all()
        for product in products:
            product.product_price = round(product.product_price - (product.product_price * discount_percentage /100),2 )

        self.db.commit()

        return products


