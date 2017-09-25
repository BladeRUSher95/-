import sys
print(sys.platform)
print('Введите последовательность чисел')
x = input().split()
k = len(x)
count = 0
for i in range(k):
    x[i] = int(x[i])
M = int(max(x))##максимальное число M в массиве - задано
buck = []
for i in range(M): ##создание нулевого массива размерности M
    buck.append(0)
j = 0
while j < k:
    buck[x[j]-1] +=1 ##увеличиваем счётчик (сложность k)
    j +=1
for i in range(M):
    if buck[i] >= 1:
        count +=1
        ##подсчитываем ненулевые элементы массива размерности M (сложность M)
print('Количество различных символов последовательности равно ', count) ##итого сложность линейная k+M

