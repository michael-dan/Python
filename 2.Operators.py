age = 15
#if (age >= 18):
#    print("You can enter")
#else:
#    print ("You cannot enter!")

age = int(input ("Enter your age"))
if (age >= 25):
    print ("You can enter alone")
elif (age>=18) and (age<25):
    print ("You can enter with your mom")
else:
    print ("You cannot enter!")
