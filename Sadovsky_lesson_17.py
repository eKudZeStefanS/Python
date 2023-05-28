class Any:
    def first(self,str_or_num):
        if type(str_or_num) == int:
            chet_count = 0
            for i in str(str_or_num):
                if int(i)%2==0:
                    chet_count += int(i)
            print(chet_count*self.second(str_or_num=str_or_num))
        elif type(str_or_num) == str:
           vowels ='aeiou'
           g_count = 0
           s_count = 0
           g_list = []
           s_list = []
           for i in str_or_num:
               if i.isalpha() and i.lower() in vowels:
                   g_count +=1
                   g_list.append(i)
               elif i.isalpha():
                   s_count +=1
                   s_list.append(i)
           if g_count*s_count <= self.second(str_or_num):
               print(*g_list)
           else:
               print(*s_list)

    def second(self,str_or_num):
        return len(str(str_or_num))

test_object = Any()
test_object.first(123)
test_object.first("adadqccv")

