employee_info = open("employees.txt", "r")

print (employee_info.readable())
print (employee_info.read())
employee_info.seek(0)
print (employee_info.readline())
print (employee_info.readlines())
#print (employee_info.readline())

employee_info.close()

employee_info = open("employees.txt", "r")

for employee in employee_info.readlines():
    print (employee)
employee_info.close()
