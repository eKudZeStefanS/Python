first_list = [5, 9, -5, 8, - 3, 1, 6, 20, -15]
sum = 0

for i in range(len(first_list)):
    if first_list[i] % 2 == 0 and first_list[i] > 0:
        sum += first_list[i]
print(sum)
