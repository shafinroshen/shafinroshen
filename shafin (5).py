#starlight
'''*****
   *****
   *****
   *****
   *****'''
size=5
for i in range(0,size):
    for j in range(0,size):
        print('*',end="")
    print()   
'''   
*
***
*****
*******
*********
**********'''     
size=12
for i in range(0,size):
    for j in range(0,i):
        print('*',end="")
    print() 
size=12       
for i in range(0,size):
    for j in range(0,i):
        print('*',end="") 
size=int(input("enter a number"))      
for i in range(0,size):
    for j in range(0,i):
        print('*',end="") 
    print()
 '''            
     *
    ***
   *****
  *******
 *********'''
 
n = 5
for i in range(1, n+1):
    for j in range(n - i):
        print(' ', end='')
    for k in range(2 * i - 1):
        print('*', end='')
    print()   
n = int(input("enter a number"))   
for i in range(1, n+1):
    for j in range(n - i):
        print(' ', end='')
    for k in range(2 * i - 1):
        print('*', end='')
    print()       
'''*********
    *******
     *****
      ***
       *'''  
n = 5
for i in range(1,n+1): 
    for j in range(n - i):
        print(' ',end='')
    for k in range():
        print('*',end='') 
    print()             