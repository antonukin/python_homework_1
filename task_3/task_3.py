'''
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

*Пример:*

385916 -> yes
123456 -> no

'''
# первый вариант
ticket_number = str(input("Введите шестизначный номер билета: "))
first_three = 0
second_three = 0
j = -1
for i in range (len(ticket_number) // 2):
    first_three += int(ticket_number[i])
    second_three += int(ticket_number[j])
    j -= 1
if first_three == second_three:
    print('Счастливый билет')
else:
    print('Вам не повезло')

# Второй вариант
ticket_number = int(input("Введите шестизначный номер билета: "))
first_three = (ticket_number // 100000) + (ticket_number // 10000 % 10) + (ticket_number // 1000 % 10)
second_three = (ticket_number // 100 % 10) + (ticket_number // 10 % 10) + (ticket_number % 10)
if first_three == second_three:
    print('Счастливый билет')
else:
    print('Вам не повезло')