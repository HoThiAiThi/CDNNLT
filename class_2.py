# def fun(variable):
#     letters = ['a', 'e', 'i', 'o', 'k']
#     if (variable in letters):
#         return True
#     else:
#         return False
# # sequence
# sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
# # using filter functionc
# filtered = list(filter(fun, sequence))
# print(filtered)

# # Return double of n
# def addition(n):
#     return n + n
# # We double all numbers using map()
# numbers = (1, 2, 3, 4)
# result = map(addition, numbers)
# print(list(result))

# nhan_doi = lambda a: a * 2
# print(nhan_doi(10))

# list_goc = [10,6,7,8,9,12,24]
# list_moi = list(filter(lambda a: (a%2==0),list_goc))
# print(list_moi)

# my_list = ["gaeks", "geeg", "keek", "practice", "aa"]
# list_moi = list(filter(lambda word: (word == word[::-1]),my_list))
# print(list_moi)

# my_list = ["gaeks", "geeg", "keek", "practice", "aa"]
# list_moi = list(filter(lambda s: all(char in s for char in ['e','a','g','k']),my_list))
# print(list_moi)

# list_goc = [10, 9, 8, 7, 6, 1, 2, 3, 4, 5]
# list_moi = list(map(lambda a: a*2 , list_goc))
# print(list_moi)

# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]
# sum_num12 = list(map(lambda x,y: x+y,nums1,nums2))
# print(sum_num12)

my_list = ["gaeks", "geeg", "keek", "practice", "aa"]
list_moi = list(filter(lambda s: all(char in s for char in ['e','g','s','k']),my_list))
print(list_moi)