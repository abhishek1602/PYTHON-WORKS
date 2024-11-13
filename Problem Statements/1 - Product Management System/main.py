from logics import Logics
from products import Product


if __name__ == "__main__":


    product1 = Product(1,"Mouse", 500)
    product2 = Product(2, "Monitor", 2000)
    product3 = Product(3, "Keyboard", 700)


    lgk = Logics()

    while True:

        print("\nOptions: (1-5)")
        print("1. Add product")
        print("2. Update product")
        print("3. View Product")
        print("4. Apply Discount")
        print("5. Save Products to csv")
        print("6. Load products from csv")
        print("7. Exit")

        choice = input("Enter The Option: ")

        if choice == '1':
            productAdd = lgk.addProduct(product1)
            productAdd = lgk.addProduct(product2)
            productAdd = lgk.addProduct(product3)
            print("Products Added: ")
            lgk.viewProducts()
            products = lgk.viewProducts()
            if products:
                for product in products:
                    print(product)

        elif choice == '2':
            uProductId = int(input("Enter Product Id: "))
            uProductName = input("Enter the name of Product: ")
            uProductPrice = input("Enter the price of the Product: ")
            result = lgk.updateProduct(uProductId, uProductName, uProductPrice)
            print(result)
            
            

        elif choice == '3':
            products = lgk.viewProducts()
            if products:
                for product in products:
                    print(product)

        elif choice == '4':
            discPercentage = float(input("Enter the percentage to apply: "))
            lgk.applyDiscount(discPercentage)
            products = lgk.viewProducts()
            if products:
                for product in products:
                    print(product)

        elif choice == '5':
            if lgk.writeProductToCsv():
                print("Products added to csv")
            else:
                print("Failed")

        elif choice == '6':
            if lgk.readProductFromCsv():
                print("Products Loaded successfully")
            else:
                print("Failed")

        elif choice == '7':
            break

        else:
            print("Invalid Option")




