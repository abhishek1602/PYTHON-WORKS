class Logics:

    def __init__(self):
        self.Products = []



    def addProduct(self, newProduct):
        for nproduct in self.Products:
            if nproduct.productId == newProduct.productId:               
                return False
        self.Products.append(newProduct)
        return True
    




    def updateProduct(self, productId, newName, newPrice):
        for uProduct in self.Products:
            if uProduct.productId == productId:
                uProduct.productName = str(newName)
                uProduct.productPrice = float(newPrice)
                print(f"Product {productId} Updated: \nName: {newName} \nPrice: {newPrice}")
                return True
        print("Product Not Found")
        return False



    def viewProducts(self):
        if not self.Products:
            print("No Products Found")
        for vProduct in self.Products:
            print(f"ProductId: {vProduct.productId} | ProductName: {vProduct.productName} | ProductPrice: {vProduct.productPrice}")
            



    def applyDiscount(self, discountPercentage):
        for dProducts in self.Products:
            discAmount = dProducts.productPrice * discountPercentage / 100
            dProducts.productPrice = round(dProducts.productPrice - discAmount,2)
        print(f"Applied {discountPercentage}% to all products")
        self.viewProducts()
        