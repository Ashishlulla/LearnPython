# Creating Empty list:

# l = []

# Taking list as a Input :

# lst = input("Enter the numbers in list separated by comma: ").split("/")
# print(lst)


# Creating list with  homogeneous values:
#
# integer_list = [1, 2, 3, 4, 5]
# string_list = ["abc", "pqr", "xyz"]
# float_list = [2.1, 3.2, 4.5 ]

# -------------------------- Creating list with heterogeneous value---------------------:

# heteregenous_list = [1, "Ashish", 2.1]

# -----------------------------casting in list (to tuple, to set)--------------------------:

# l1 = tuple([1,2,4,5,1,2,4,5])
# print(type(l1))
# l2 = set([1,2,4,5,1,2,4,5])
# print(type(l2))


# Append, concatenation, extend function in list:

# l1 = [1,2,3,4,5]
# l2 = [6,7,8,9]
# ---------------------Append----------------------:
# l1.append(l2)
# print(l1)
# -------------------- Extend------------------------ :
# l1.extend(l2)
# print(l1)
# ----------------concatenation--------------------:
# l1 = l1+l2
# print(l1)

# -----------------Sort() , reverse(), sorted()-----------:
#
# lst = [2,43,6,3,6,3,64,32,435,32]
# lst.sort()
# print(lst)

# print(sorted(lst))

# l.reverse()
# print(l)

# Insert , index , remove, overwrite element

# --------Indexes---------:
# +ve  0  1  2  3  4  5
# lst = [1, 2, 3, 4, 5, 6]
# -ve -6 -5 -4 -3 -2 -1

# print(l.index(2))

# lst.insert(2,0)  # insert(position, value)
# print(lst)

# lst.remove(5)
# print(lst)

# lst[0] = 10
# print(lst)

# clear, copy, count

# a = [1, 1, 1, 12, 2, 2, 2, 24, 3, 3, 2, 26, 5, 4, 3, 2, 2, 2, 2]
# b = a.copy()
# print(b)

# print(a.count(2))

# a.clear()
# print(a)


# Slicing In list :
#
# lst = [1, 2, 3, 4, 5, 6, 7, 8]
# # print(lst[2:5]) #output = [3,4,5]
# # print(lst[::-1])  # output = [8, 7, 6, 5, 4, 3, 2, 1]

# -------------------Looping In List---------------------------

# ------------------for loop (to get direct value)--------------------
# lst = [1, 2, 3, 4, 5, 6, 7, 8]

#  ------------------for loop (to get value through index)--------------------

# lst = [1, 2, 3, 4, 5, 6, 7, 8]

# ----------------------- Enumerate Func() ------------------------------

# lst = [1, 2, 3, 4, 5, 6, 7, 8]

# --------------------List Comprehension-------------------------

# syntax : [output   looping   expression]
# lst = ["abc", "xyz", "pqr", "jkl", "def"]
# lst1 = []
# for i in lst:
#     lst1.append(i)

# print(lst1)

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# even =[]
# odd = []
# for i in lst:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)

# print(even)
# print(odd)
