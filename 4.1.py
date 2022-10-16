from random import randint
massive = []
trenk = int(input('Введите размерность массива:'))
trenk2 = str(input( 'Элементы массива генерируются случайно или вводятся пользователем? Рандом/ввод вручную '))
k = trenk
if trenk2 == 'рандом' :
    while trenk > 0:
        massive.append(randint(-1000000,1000000))
        trenk = trenk - 1
if trenk2 == 'ввод вручную':
    num = 1
    while trenk > 0:
        element = float(input('Введите '+str(num)+' элемент массива'))
        massive.append(element)
        trenk = trenk - 1
        num = int(num)+1
maximum = -1000000
for i in range(len(massive)):
    if massive[i] > maximum:
        maximum = massive[i]   
for i in range(len(massive)):
    if massive[i] == maximum:
        for e in range(i + 1, k):
            massive.pop(e)
            massive.insert(e,0)
print(massive)
        
