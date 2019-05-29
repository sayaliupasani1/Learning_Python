candidates = ["a", "b", "c", "d"]
votes = ["a", "b", "a", "d", "a"]

count_a=0
count_b=0
count_c=0
count_d=0

for vote in votes:
    if vote == "a":
        count_a+=1
    elif vote == "b":
        count_b+=1
    elif vote == "c":
        count_c+=1
    else:
        count_d+=1

if count_a > count_b and count_a >count_c and count_a > count_d:
    print ("The winner is candidate a with total votes of "+str(count_a)+ ".")
elif count_b > count_a and count_b > count_c and count_b > count_d:
    print("The winner is candidate b with total votes of "+str(count_b)+ ".")
elif count_c > count_a and count_c > count_b and count_c >count_d:
    print("The winner is candidate c with total votes of "+str(count_c)+ ".")
else:
    print("The winner is candiate d with total votes of " +str(count_d)+ ".")