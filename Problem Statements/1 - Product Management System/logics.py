#All functions in logic must return to the caller, either data or status messages
import csv
from products import Product
class Logics:

    def __init__(self):
        self.products = []


    def addProduct(self, newProduct):
        for nproduct in self.products:
            if nproduct.productId == newProduct.productId:               
                return False
        self.products.append(newProduct)
        self.viewProducts()
        return True
    


    def updateProduct(self, productId, newName, newPrice):
        for uProduct in self.products:
            if uProduct.productId == productId:
                uProduct.productName = str(newName)
                uProduct.productPrice = float(newPrice)
                return f"Product Updated with Id: {productId},  ProductName: {newName}, ProductPrice {newPrice}"
            return f"Product Not found"
        



    def viewProducts(self):
        return self.products


    def applyDiscount(self, discountPercentage):
        
        for dProducts in self.products:
            discAmount = dProducts.productPrice * discountPercentage / 100
            dProducts.productPrice = round(dProducts.productPrice - discAmount,2)      
        self.viewProducts()
        
    def writeProductToCsv(self, filename = 'products.csv'):
        final = False
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['productId', 'productName', 'productPrice'])
            for product in self.products:
                writer.writerow(product.writeToCsv())
                final = True
        return final
                


    def readProductFromCsv(self, filename = 'products.csv'):
        self.products.clear()
        final = False
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                self.products.append(Product.readFromCsv(row))
                final = True
        return final