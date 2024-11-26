#All functions in logic must return to the caller, either data or status messages
import csv
from products import Product
import sqlite3

class Logics:
    def __init__(self):
        self.db_file = "products.db"

    def connect_db(self):
        return sqlite3.connect(self.db_file)

    def addProduct(self, newProduct):
        conn = self.connect_db()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO products (productId, productName, productPrice) VALUES (?, ?, ?)", 
                           (newProduct.productId, newProduct.productName, newProduct.productPrice))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            conn.close()

    def updateProduct(self, productId, newName, newPrice):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE products 
            SET productName = ?, productPrice = ? 
            WHERE productId = ?
        """, (newName, newPrice, productId))
        conn.commit()
        rows_updated = cursor.rowcount
        conn.close()
        if rows_updated > 0:
            return f"Product Updated with Id: {productId}, ProductName: {newName}, ProductPrice: {newPrice}"
        return "Product Not Found"

    def viewProducts(self):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        conn.close()
        return [Product(*row) for row in rows]

    def applyDiscount(self, discountPercentage):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()

        updated_products = []
        for row in rows:
            productId, productName, productPrice = row
            newPrice = round(productPrice - (productPrice * discountPercentage / 100), 2)
            cursor.execute("""
                UPDATE products 
                SET productPrice = ? 
                WHERE productId = ?
            """, (newPrice, productId))
            updated_products.append(Product(productId, productName, newPrice))
        conn.commit()
        conn.close()
        return updated_products
