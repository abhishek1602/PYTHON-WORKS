from logics import Logic
from db import Database
from user import User

def main():
    
    logics = Logic()
    

    try:

        user1 = User(userName="Abhishek", userAge=22, userEmail="abhishekmanjhi.1602@gmail.com")
        user2 = User(userName="Abhi", userAge=30, userEmail="abhi@gmail.com")
        success = logics.insert(user1.userName, user1.userAge, user1.userEmail)
        print(f"User added successfully {success}")
        success = logics.insert(user2.userName, user2.userAge, user2.userEmail)
        print(f"User added successfully {success}")


        users = logics.getLogics()
        print("\nFetching Data: ")
        for user in users:
              print(user)


    except Exception as e:
            print(f"An error occured {e}")


    finally:

            clean = logics.cleanUp()
            print(f"Data cleaned: {clean}")


if __name__ == "__main__":
    main()
        
        








