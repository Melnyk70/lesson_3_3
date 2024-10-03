# ДЗ 3.3. Розділити один список на два списки
# 4 варіанти даних для вибору:
#numbers=[]
#numbers=[111]
#numbers=[1,2,3,4,5,6]
numbers=[1,2,3,4,5,6,7]
# програма:
len_numbers = len(numbers) #довжина списку
len_numbers1=len_numbers%2 #значення для визначення парної або непарної кількості елементів
len_numbers2=len_numbers//2 #значення для визначення парної або непарної кількості елементів
if len_numbers == 0:
   numbers1=numbers
   numbers2=numbers
   numbers3=[numbers1,numbers2]
   print(numbers,"=>",numbers3)
elif len_numbers1 ==0:
   numbers1=numbers[0:len_numbers2:1]
   numbers2=numbers[len_numbers2:numbers[-1]:1]
   numbers3=[numbers1,numbers2]
   print(numbers,"=>",numbers3)
elif len_numbers1 ==1:
   numbers1=numbers[0:len_numbers2+1:1]
   numbers2=numbers[len_numbers2+1:numbers[-1]:1]
   numbers3=[numbers1,numbers2]
   print(numbers,"=>",numbers3)
else:
   print("Щось пішло не так :-)")