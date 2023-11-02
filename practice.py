import datetime
now = datetime.datetime.now()
print ("Current login status : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

q1 = input("Full Name: ")
print(q1)

age = int(input("age: "))
if age >10:
    print("this should be easy for you")
elif age <10:
    print("i will challenge you")

print(age)
print ("okay, lets begin the test...(addition)")

q3 = ("what is 9+7? ")
if int(input (q3)) == 16: 
    print ("well done!")
else:
    print ("incorrect, :( ")

print ("okay try a harder one...")

q4 =("what is 47+53? ")
if int(input(q4)) == 100 : 
    print ("superb!")
else: 
    print("incorrect,thats a bummer!")

print ("lets move on to subtraction...")

q5=("what is 11-6? ")
if input (q5) == "5" : 
    print ("well done!")
else:
    print ("incorrect, try harder! :( ")