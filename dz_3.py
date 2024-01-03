print('Эта программа выводит на экран таблицу умножения, укажите диапозон:')
num1 = int(input('Начало диапозона:'))
num2 = int(input('Конец диапозона:'))

for i in range(num1, num2 + 1):
    for j in range(1, 11):
        print(i, "*", j, "=", i * j)
        print( )
        