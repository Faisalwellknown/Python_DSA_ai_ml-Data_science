"""print (9>10)"""

a = 5
b = 10
if a > b :
    print("a is greater than b") 
else :
    print("b is greater than a")

print(bool("Hello"))
print(bool(15))


x = "Hello"
y = 15

print(bool(x))
print(bool(y))




class myclass():
    def __len__(self):
        return 0
    

myobj = myclass()
print(bool(myobj))