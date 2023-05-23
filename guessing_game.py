from random import randint 

print('Я загодал число. От 1 до 10. Угадай его!')
chislo = randint(1, 11)
th_back_number = int(input('Введите число: '))

while chislo != th_back_number:
    th_back_number = int(input('Попробуй заново: '))
    if chislo < th_back_number:
        print('Число больше моего!')
    elif chislo > th_back_number:
          print('Число меньше моего!')
    else:
          print('Поздравляю вы угадали число:', chislo,'!')

