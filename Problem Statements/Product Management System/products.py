class Products:
    def __init__(self, productId, productName, productPrice):
        self.productId = productId
        self.productName = productName
        self.productPrice = float(productPrice)
        
    def __str__(self):
        return f"ProductId: {self.productId}, ProductName: {self.productName}, ProductPrice: {self.productPrice}"