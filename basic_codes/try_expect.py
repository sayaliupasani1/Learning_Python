try:
    value = 10/0
    i = int(input("Enter your number: "))
    print (i)
except ValueError:
    print ("Invalid input")
except ZeroDivisionError as x:
    print (x)
    #print ("Divide by zero is not allowed")