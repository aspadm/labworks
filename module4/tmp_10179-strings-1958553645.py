# Кириллов Алексей, ИУ7-12
# Из введённых латиницей слов вывести в алфавитном порядке буквы,
# встречающиеся в каждом из слов

words = list(input("Введите строку: ").split())

letters = set(words[0][:])

for i in range(len(words)):
    letters = letters&set(words[i][:])
    
letters = list(letters)

print("Буквы, встречающиеся в каждом из слов, в алфавитном порядке:") 
for i in range(len(letters)):
    print(letters[i],end="")
