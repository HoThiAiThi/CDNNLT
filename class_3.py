def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False
# sequence
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
# using filter functionc
filtered = filter(fun, sequence)
# # chars =['a','b','c']
# # for idx, char in enumerate(chars):
# #     if char == 'b':
# #         chars[idx] = 'e'
# # print(chars)
# with open('romeo.txt', 'r') as file:
#     lines = file.readlines()
# # print(lines)
# unique_word =[]
# for line in lines:
#     words = line.split()
#     for word in words:
#         if word not in unique_word:
#             unique_word.append(word)
# unique_word.sort()
# for word in unique_word:
#     print(word)
# letters = ['a', 'b', 'c', 'd']
# print(letters)
# upper_letters = []
# for letter in letters:
#     result = letter.upper()
#     upper_letters.append(result)
# print(upper_letters)
# upper_list = [x.upper() for x in letters]
# print(upper_list)
# number = [1, 34, 5, 7, 3, 57, 356]
# print(number)
# double_number = [x * 2 for x in number if x > 10]
# print(double_number)
# list_num = [x * 2 if x >10 else x * 5 for x in number]
# print(list_num)

# mỗi phần tử cộng thêm 6
# number = [1, 34, 5, 7, 3, 57, 356]
# print(number)
# new_list = [x +6  for x in number]
# print(new_list)

#  bình phương x lớn hơn 50
# num =[2,7,8,10,12,15]
# print(num)
# new_list=[x for x in num if x*x > 50]
# print(new_list)

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
print (fruits)
new_fruits =[x for x in fruits if len(x)> 5 ]
print(new_fruits)
new_fruits_a = [x for x in fruits if 'a' in x ]
print(new_fruits_a)
new_fruits_aa = [x for x in fruits if x.count('a') >2]
print(new_fruits_aa)