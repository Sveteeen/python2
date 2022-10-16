from random import randint
massive = []
trenk = int(input('Введите размерность массива:'))
trenk2 = str(input( 'Элементы массива генерируются случайно или вводятся пользователем? Рандом/ввод вручную '))
if trenk2 == 'рандом' :
    while trenk > 0:
        massive.append(randint (-1000000,1000000))
        trenk = trenk - 1
if trenk2 == 'ввод вручную':
    num = 1
    while trenk > 0:
        element = float(input('Введите '+str(num)+' элемент массива'))
        massive.append(element)
        trenk = trenk - 1
        num = int(num)+1
massive2 = []
trenk2 = int(input('Введите размерность массива2:'))
trenk22 = str(input( 'Элементы массива2 генерируются случайно или вводятся пользователем? Рандом2/ввод вручную2 '))
if trenk22 == 'рандом2' :
    while trenk2 > 0:
        massive2.append(randint (-1000000,1000000))
        trenk2 = trenk2 - 1
if trenk22 == 'ввод вручную2':
    num2 = 1
    while trenk2 > 0:
        element2 = float(input('Введите '+str(num2)+' элемент массива'))
        massive2.append(element2)
        trenk2 = trenk2 - 1
        num2 = int(num2)+1
print(massive)
print(massive2)
massive3= []        
for i in range(len(massive)):
    for e in range(len(massive2)):
        if massive[i] == massive2[e]:
            massive3.append(massive[i])
print(massive3)            
        
