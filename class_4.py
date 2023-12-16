my_list = ["gaeks", "geeg", "keek", "practice", "aa"]
list_moi = list(filter(lambda s: all(char in s for char in ['e','g','s','k']),my_list))
print(list_moi)