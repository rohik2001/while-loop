rohik=1
while rohik<=10 :
    print('rohik: ',rohik)
    rohik=rohik+1
#num
num=1
total=0
while num<=10:
    total=total+num
    num=num+1
print('total: ', total)

# factorial
n=5
factorial=1
while n>0:
    factorial=factorial*n
    n=n-1
    print("factorial is : ",factorial);

password='admin'
user_input=""
while user_input != password:
    user_input=input("Enter your password: ")
    if user_input==password:
        print("access granted")
        break
    else:
        print("access denied")




# take input from the user 
num = int(input("Enter a number: "))
# initialize sum
sum = 0
# find the sum of the cube of each digit
temp = num
while temp>0:
    digit=temp % 10
    sum += digit ** 3
    temp //= 10
# display the result 
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")