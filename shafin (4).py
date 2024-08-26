#makima
input1=input('enter a value ')
for value in input1:
    if value.isupper():
        print(value)
input2=input('enter a value')
upper=0
lower=0
for value in input2:
    if value.islower():
        lower=lower+1
    else:
        print(value) 
    print(input2)    
def deadpool(input2):
    upper=0
    lower=0
    num=0
    for value in input2:
        if value.islower():
            lower=lower+1
        elif value.isupper():
            upper=upper+1
        else:
            num=num+1    
    return upper,lower 
deadpool(input2)
list1=[1,2,3,4,5,6] 
def alia(n):
    return n+10
list(map(alia,list1))
list2=[1,2,3,4,5,6] 
def mrunal(n):
    return n*n
list(map(mrunal,list2))
allu=[10,20,30,40,50]
sum=0
def kohli(allu):
    for value in allu:
      sum=sum+value
    return sum

def bublebee(a,b):
    return a+b
import  functools 
print(functools.reduce(bublebee,allu))
print(functools.reduce(lambda a,b:a+b,allu))
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b,allu))
    
   
    
                 