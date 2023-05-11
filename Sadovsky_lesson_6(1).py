

first_list = [5, 9, -5, 8, - 3, 1, 6, 20, -15]
s = 0

for i in range(len(first_list)):
    if first_list[i] % 2 == 0 and first_list[i] > 0:
        s += first_list[i]
print(s)

my_list = [90, 230, 55, 68, 98, 23, 45, 53]
mean = sum(my_list)/len(my_list)
print(mean)
for i in my_list:
    if i < mean:
     print(i)
else:
    i =+ 1