def class_10(*students):
    print(students)
    for i in students:
        print(i)
class_10("ram","sara","Pradeep")

#Keyword arguents fucntions in python

def message(name,age):
    print(name,"age is ",age)
message(name="ram",age=25)

#arbitay keyword arguements in python
def biodata(**data):
    print(data)
biodata(name='ram',gender='male',age=24)

#defautlt parameter function in python
def user(name,city="salem"):
    print(name,"and he is form", city)
user(name="pradeep",city="oddancahtram")
user(name="nivetha")

#passing a list as an argument in function python.
def total(marks):
    return(sum(marks))

print(total([20,43,45]))

#recursie function calling itself is called recursive function

def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))


print(factorial(5))