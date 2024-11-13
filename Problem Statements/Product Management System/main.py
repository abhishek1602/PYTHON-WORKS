from logics import Logics
from products import Products


if __name__ == "__main__":


    product1 = Products(1,"Mouse", 500)
    product2 = Products(2, "Monitor", 2000)
    product3 = Products(3, "Keyboard", 700)


    lgk = Logics()

    while True:

        print("\nOptions: (1-5)")
        print("1. Add product")
        print("2. Update product")
        print("3. View Product")
        print("4. Apply Discount")
        print("5 to Exit")

        choice = input("Enter The Option: ")

        if choice == '1':
            productAdd = lgk.addProduct(product1)
            productAdd = lgk.addProduct(product2)
            productAdd = lgk.addProduct(product3)
            print("Products Added")
            lgk.viewProducts()

        elif choice == '2':
            uProductId = int(input("Enter Product Id: "))
            uProductName = input("Enter the name of Product: ")
            uProductPrice = input("Enter the price of the Product: ")
            lgk.updateProduct(uProductId, uProductName, uProductPrice)

        elif choice == '3':
            lgk.viewProducts()

        elif choice == '4':
            discPercentage = float(input("Enter the percentage to apply: "))
            lgk.applyDiscount(discPercentage)

        elif choice == '5':
            print("Program Exited")
            break

        else:
            print("Invalid Option")




