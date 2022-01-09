# Creating Empty Dictionary
# dic = {}
# print(type(dic))

# Creating Dictionary With Key and Values:
# dic = {
#   "brand": "Tata",
#   "model": "Harrier",
#   "year": 2017
# }
# print(dic)

# Length of Dictionary:
#
# dic = {
#   "brand": "Tata",
#   "model": "Harrier",
#   "year": 2017
# }
# print(len(dic))

# Accessing Dictionary Items (Through Key):
# dic = {
#   "brand": "Tata",
#   "model": "Harrier",
#   "year": 2017
# }
# print(dic["brand"])

# Accessing Dictionary Items (Through .Get()):
# dic = {
#   "brand": "Tata",
#   "model": "Harrier",
#   "year": 2017
# }
# print(dic.get("brand"))

# Get Keys, Values, Items of Dictionary

# dic = {
#   "brand": "Tata",
#   "model": "Harrier",
#   "year": 2017
# }
# print(dic.keys())
# print(dic.values())
# print(dic.items())

# Checking the presence of Key :

# dic = {
#   "brand": "Tata",
#   "model": "Harrier",
#   "year": 2017
# }
# if "Tata" in dic.values():
#     print("Present")
# else:
#     print('Not Present')

# Change values in Dictionary(Naive Method), update():
dic = {
  "brand": "Tata",
  "model": "Harrier",
  "year": 2017
}
# dic["name"] = "Ashish"
# print(dic)
# dic.update({"name":"Ashish"})   # dic_name.update({key:value})
# print(dic)

# Deleting Dictionary Items :
# dic = {
#   "brand": "Tata",
#   "model": "Harrier",
#   "year": 2017
# }
# dic.pop("model")
# print(dic)

# dic.popitem()
# print(dic)
# dic.popitem()
# print(dic)
# using del keyword

# del dic["model"]
# print(dic)

# del dic
# print(dic)

# # Clear()
#
# dic.clear()
# print(dic)


# Looping In Dictionary:

# dic = {
#   "brand": "Tata",
#   "model": "Harrier",
#   "year": 2017
# }
# for x in dic:
#     print(x)

# for i in dic.keys():
#     print(i)

# for i in dic.values():
#     print(i)

# for key , val in dic.items():
#     print(f"Keys : {key}\n"
#           f"value: {val}")

# Nested Dictionary:
#
# students = {
#   "s1" : {
#     "name" : "abc",
#     "age" : 10
#   },
#   "s2" : {
#     "name" : "def",
#     "age" :  7
#   },
#   "s3" : {
#     "name": "xyz",
#     "age": 11
#   }
# }
# print(students["s2"]["name"])


# Nested Dictionary:
#
# main_dic = {
#   "sub_dic1":{"name":"Ashish",
#             "age": 20},
#
#  "sub_dic2":{"name":"Bhavesh",
#             "age":21},
#
#  "sub_dic3":{"name":"Somesh",
#             "age":22}
# }
# print(main_dic["sub_dic3"]["age"])

# nested_dictionar = {{},{},{},{},{},{}}


