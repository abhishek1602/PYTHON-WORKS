# # num = [1,2,3,4]

# # def doubleit(num):
# #     print("Hello")
# #     return num**2

# # ok = list(map(doubleit, num))
# # print(ok)

# x = ["hello", "hey"]
# z = ["hello", "He"]

# y = filter(lambda x : len(x)>=3, x)
# m = filter(lambda z : len(z)>=4, z)


# print(list(y))
# print(list(m))


# def hari(z):
#     return len(z)>=3

# def hari1(x):
#     return len(x)>=4

# y = filter(hari1, x)
# m = filter(hari, z)
# print(list(y))
# print(list(m))


a = [{1:"Abhishek"}, {4: "Kamlesh"}, {2: "Chaitanya"}, 
     {6: "Darshini"}, {3: "Prajakta"}, {5:"Keerthna"}]

def sort_kr(a):
    return list(a.keys())[0]

sortA = sorted(a, key = sort_kr)

print(sortA)
    

sortB = sorted(a, key=lambda a: list(a.keys())[0])
print(sortB)