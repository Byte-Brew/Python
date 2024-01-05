# STRING

s="hello world"[::-1]
print(s)

s="hello world"
print(s.replace("hello world","New"))
print(s)

s1="First"
s2="Second"
print(s1 +" "+ s2)

s1="Hello World"
a=s1.find('s')
print(a)
# if a==(-1);
#     print("False")
# else:
# print("True")

s1="Hello World"
print(s1.split())


# DICTIONRY

s={'key1':10,'key2':20,'key3':30}
sujal={
    'address':{
        'key7':20
}
}
s.update({'key4':40})
print(s)
s.popitem()
print(s)
s.pop('key2')
print(s)
s_new=s.copy()
print(s_new)
print(s_new.get('key1'))
print(sujal['address']['key7'])

s1={'k1':10,'k2':20}
s2={'k3':30,'k4':40}
s3=s1.copy()
s3.update(s2)
print(s3)



a=int(input("Enter Number: "))

l=list()
for i in range(1,11):
    s=a*i
    l.append(s)

print(l)


Employee={
    'Employee_ID':input('Enter Employee ID : '),
    'Employee_Name':input('Enter Employee Name :'),
    'Employee_Salary':int(input('Enter Employee Salary :')),
    'Employee_Departmet':input('Enter Employee Departmet :')
}
print(Employee)