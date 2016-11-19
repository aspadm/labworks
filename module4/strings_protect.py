# Кириллов Алексей, ИУ7-12
# Защита: найти в строке все слова, в которых каждая буква встречается
# больше одного раза. Вывести эти слова в обратно алфавитному порядке.

S = list(input('Введите строку: ').split())
K = list()

for i in range(len(S)):
    nn = True
    z = set(S[i])
    for j in z:
        if S[i].count(j) < 2:
            nn = False
    if nn:
        K.append(S[i])

for i in range(len(K)-1,0,-1):
    for j in range(i):
        if K[i] > K[j]:
            K[i],K[j] = K[j],K[i]

print('Слова в обратно-алфавитном порядке, каждая буква встречается чаще 1:')
for i in range(len(K)):
    print(K[i],end=' ')
