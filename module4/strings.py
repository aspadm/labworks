# Кириллов Алексей, ИУ7-12
# Вариант 5: из введённых латиницей слов вывести в алфавитном порядке
# согласные буквы, встречающиеся в каждом из слов. 

words = list(input("Введите строку: ").split())

letters = set(words[0][:]) - \
    {'a','A','e','E','i','I','o','O','u','U','y','Y'}

for i in range(len(words)):
    letters = letters&set(words[i][:]) 

letters = list(letters)

for i in range(len(letters)-1,0,-1):
    for j in range(i):
        if letters[i] < letters[j]:
            letters[i],letters[j] = letters[j],letters[i]


print("Буквы, встречающиеся в каждом из слов, в алфавитном порядке:")
for i in range(len(letters)):
    print(letters[i],end="")
