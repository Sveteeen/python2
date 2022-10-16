massive = []
rey_1 = int(input('Введите количество элементов в заданном массиве:'))
num = 1
while rey_1 > 0:
    element = int(input('Введите '+ str(num)+ ' элемент массива:'))
    massive.append(element)
    rey_1 = rey_1 - 1
    num += 1
minimum = 9999999
for i in range(len(massive)):
    mmm = massive[i]
    if mmm < minimum:
        minimum = mmm
rey_2= int(input('Введите число на которое отличается минимальный элемент массива:'))
count = 0
for i in range(len(massive)):
    if massive[i] - rey_2 == minimum:
        count = count + 1
print('Количество элементов в заданном массиве, отличающихся от минимального элемента массива на delta: ', count)           
    
    
    

