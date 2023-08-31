# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions.

import fractions
import decimal

n=fractions.Fraction(2657,21) #для проверки
m=fractions.Fraction(11442,11) #для проверки
n1='2657/21'
m1='11442/11'

n1=n1.split('/')
a=[i for i in n1]
a1=int(a[0])
b1=int(a[1])
#print(a1,b1)

m1=m1.split('/')
b=[i for i in m1]
a2=int(b[0])
b2=int(b[1])
#print(a2,b2)

#Находим НОД для произведения
s1=a1*a2
s2=b1*b2
while s1!=s2:
    if s1>s2:
        s1=s1-s2
    else:
        s2=s2-s1
#print(f'НОД равен - {s1}')
pr=(f'{(a1*a2)//s1}/{b1*b2//s1}' if (b1*b2//s1)>1 else (a1*a2)//s1)
print(f'Произведение равно {pr}')

#Находим наименьшее общее кратное для сложения
a3=a1*b2+a2*b1
b3=b1*b2
while a3!=b3:
    if a3>b3:
        a3=a3-b3
    else:
        b3=b3-a3
nok=a3*b3//a3
#print(f'НОК равен - {nok}')
sum_dr=(f'{(a1*b2+a2*b1)//nok}/{b2*b1//nok}' if (b2*b1//nok)>1 else (a1*b2+a2*b1)//nok)
print(f'Сумма равна {sum_dr}')

print()
print(f'ПРОВЕРКА: произведение равно {n*m}')
print(f'ПРОВЕРКА: сумма равна {n+m}')

