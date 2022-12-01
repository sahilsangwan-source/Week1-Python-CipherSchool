print('hello world')
var="sahil"
print(var)
sar,num="sangwan",0
print(sar)
print(num)
#user input
#input function
name =input("type your name ") #input takes string
print("hello" +name)
age=input("what is your age") #18   #18 is taken as string
print("your age is ",age)  #output> your age is 18 
str1=str(input())  #   #takes string  from user
num1=int(input()) #takes integer from user
num2=float(input()) #takes float number from user
print(str1+num1) # gives error, cannot concatinate str and int/float
print(num1+num2) # gives float number
#multiple inputs
name,age,address=input("enter your date and month ").split() # used to take multiple inputs 
print(name)
print(age)
print(address)

#string formatting
name="sahil"
age=24
print("hello {} your age is {}".format(name,age)) #python 3
print(f"hello {name} your age is {age}") #currently used, best


# string indexing
str1= "python"
#positions(index number)
# p=0 , -6
# y=1 , -5
# t=2 , -4
# h=3 , -3
# o=4 , -2
# n=5 , -1
print(str1[1]) #output will be "y"
#slicing/selecting sub sequences
#syntax - varaible[start argument:stop arguement] 
print(str1[1:4])  #prints all the indexes from 1 to 4-1
print(str1[-3:6])
print([str1[:3]]) #prints from 0 to 3-1

#step arguement
print("sahil[0:3:1]") #here 1 is step 
print("sahil"[0:5:2] )
print('sahil'[::-1])  #reverses the string

#string methods
name1="SAhIl sAnGwan"
#1 len() function
print(len(name1)) #gives length of string
#2 lower() method
print(name1.lower()) #gives dtring in lowercase
#3 upper() method
print(name1.upper()) #gives string in upper case
#4 title() method
print(name1.title()) #gives first character in uppercase and remaining in lowercase
#5 count() method case sensitive
print(name1.count("s")) #counts how many times character is used 

#strip method
name2="   sahil  "
dots="............"
#lstrip() and rstrip()  method
print(name + dots)
print(name2.lstrip()+dots) #removes spaces from left
print(name2.rstrip()+dots) #removes spaces from right
print(name2.strip()+dots)   #removes spaces from lest and right
#replace() method
print(name2.replace(" ","")+dots) #replaces spaces with no space

#center method
name3="sahil"
#**sahil**,10
print(name3.center(len(name3)+4,'*')) #
#if else condition,else comes after if conditiion
#example
age=int(input())
if age>14:
    print("your are above 14")
else:
    print("you are below 14 ")

#pass statement skips the whole condition and prints nothing
if age<14:
    pass
#nested if else
a=24
b=int(input())
if a==b:
    print('you win')
else:
    if a<b:
        print('too low')
    else:
        print('too high')

#if elif else statement used for multiple conditions
#example
# show ticket pricing
# 1 to 3 (free)
# 4 to 10 (150)
# 11 to 60 (250)
# above 60 (200)
Age=int(input())
if 0<Age<=3:
    print('ticket price : Free')
elif 3<Age<=10:
    print('ticket price : 150 ')
elif 10<Age<=60:
    print('ticket price : 250 ')
else:
    print('ticket price : 200 ')


#check empty or not
# example
nam=input()
if nam:             #true if string input
    print('str is not empty')
else:
    print('string is empty')