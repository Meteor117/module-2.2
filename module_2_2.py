a=int(input("Введите любое число, "))
b=int(input("Введите любое число, "))
c=int(input("Введите любое число, "))
if a==b and a==c and b==c and b==a:#все числа равны между собой
    print(3)
elif a==b or b==c or a==c: #два из трех чисел равны между собой
    print(2)
else: #ни одно из чисел не равно между собой
    print(0)