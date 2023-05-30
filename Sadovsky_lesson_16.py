def modify_list(l): l[:] = [i//2 for i in l if i%2==0]
lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))
print(lst)
modify_list(lst)
print(lst)
lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)
lst = [100,200,4343,15,12]
print(modify_list(lst))
print(lst)