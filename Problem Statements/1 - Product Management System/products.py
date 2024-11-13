

class Product:
    def __init__(self, productId, productName, productPrice):
        self.productId = productId
        self.productName = productName
        self.productPrice = float(productPrice)
        
    def __repr__(self):
        return f"Product({self.productId},{self.productName},{self.productPrice})"
    
    def writeToCsv(self):
        return [self.productId, self.productName, self.productPrice]
    

    @classmethod
    def readFromCsv(cls, row):
        productId, productName, productPrice = row
        return cls(int(productId), productName, float(productPrice))
    




    
