tup_2 = (20, 5, 1, 9, 3 ,45)

sorted_tup = sorted(tup_2)
print(sorted_tup)
print(type(sorted_tup))

random_list = (3, 4, 66, 77, 33)
combine_list = sorted(sorted_tup + random_list)
print(combine_list)
print("\n")
new_tup = tuple(combine_list)
print(type(new_tup))
print(new_tup)