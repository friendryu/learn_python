# 1) check wheter a number  is greater than 0 or not
# 2) check wheter a number  is positive or negative 
# 3) print a message if the condition is true
# a=-10
# if(a>=0) :
#     print('number is positive')
# print('program over!!')
# ------------------------------------
# 4) simple if-else program
# a=int(input('enter number: '))
# if(a>=0) :
#     print('number is positive')
#     print('the if is true')
# else:
#     print('number is negative')
#     print('the else is true')
# ------------------------------------
# 5) check if the number is odd or event
# a=int(input('enter number: '))
# if(a%2==0) :
#     print('number is even')
#     print('the if is true')
# else: #(a%2!=0)
#     print('number is odd')
#     print('the else is true')
# ------------------------------------
# if-elif-else statements in python.
# number is positive or negative or zero
# which number is greater out of 3 numbers

# finding out the grade of a student
# a=int(input("enter the number:"))
# if(a>0):
#     print('number is +ive')
#     print('> zero')
# elif(a<0):
#     print('number is -ive')
#     print('< zero')
# else:
#     print('number is zero')
#     print('== 0')    
# ------------------------------------
# a=int(input("enter the 1st number:"))
# b=int(input("enter the 2nd number:"))
# c=int(input("enter the 3rd number:"))
# d=int(input("enter the 4th number:"))

# if(a>b) and (a>c) and (a>d):
#     print('a is the biggest number')
# elif(b>a) and (b>c) and (b>d):
#     print('b is the biggest number')
# elif(c>a) and (c>b) and (c>d):
#     print('c is the biggest number')
# else:
#     print('d is the biggest number')
# ------------------------------------
# finding out the grade of a student

# marks <35 and >=0 fail
# marks >=35 and <40 pass
# marks >=40 and <50 average
# marks >=50 and <60 above average
# marks >=60 and <70 good
# marks >=70 and <80 very good
# marks >=80 and <=100 excellent

# marks=int(input("Enter the marks of the student: "))
# if(marks<35) and (marks>=0):
#     print("fail")
# elif(marks>=35) and (marks<40):
#     print("pass")
# elif(marks>=40) and (marks<50):
#     print("average")
# elif(marks>=50) and (marks<60):
#     print("above average")
# elif(marks>=60) and (marks<70):
#     print("good")
# elif(marks>=70) and (marks<80):
#     print("very good")
# elif(marks>=80) and (marks<=100):
#     print("excellent")
# else:
#     print("the student absent")
# ------------------------------------
# nested if -else in python
# one if inside another if is called nested if statement in python
# to check whether an individual is male or female voter

age=int(input("enter the age: "))
g=input("enter the gender:")

if(age>=18):
    if(g=='F'):
        print("Female Voter")
    else:
        print("Male Voter")
else:
    print("individual is not eligibel")











