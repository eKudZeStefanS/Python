






































































string = input("Введите строку: ")
print(string)

words = string.split()

id_longest = 0
for i in range(1, len(words)):
    if len(words[id_longest]) < len(words[i]):
        id_longest = i
print(words[id_longest])

s = input('Введите текст: ')

t = tuple(map(str, s.split()))

print(t)