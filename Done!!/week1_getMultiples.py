#Done getMultiples

# write a function that takes a number and returns the dictionary that has 3 keys
# statuscode: 1 // in case multiples are got
# statusmessage: got successfull or failed
# data: which have  the array that contains 5 multiples
# if input passed is 0. then
# statuscode: -1
# statusmessage: failed to get multiples because input is zero
# data: none

userInput = int(input("Enter the number: "))

def getMultiples(userInput):

    zeroDict = {
        "statuscode" : -1,
        "statusmessage" : "failed",
        "data": None
    }

    multiples = [userInput * i for i in range(1,6)]

    numDict = {
        "statuscode": 0,
        "statusmessage": "success",
        "data": multiples
    }

    if userInput == 0:
        print(zeroDict)

    else:
        print(numDict)

getMultiples(userInput)