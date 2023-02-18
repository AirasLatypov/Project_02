# with open('content.txt', encoding="utf-8") as text:
#     while text.readline() >= 1:
#         mystring = text.readline()
#         print(mystring)


myfile = open("content.txt", "r", encoding="utf-8")
for line in myfile:
    print(line)
myfile.close()

# spisok = ['Hwllo', 123124124, "kjHjkhk", True, 3.4365, ["aaa", "bbb", ['Hwllo', 123124124, "kjHjkhk", True, 3.4365, ["aaa", "bbb", "ccc"], 8888]], 8888]
#
# element = spisok[5][2][5][2]
#
# print(element)
# print(type(element))



# float()
# str() string
# int() integer
# bool() Boolean
# list()

# data = "Hello everyone, I am python developer"
# print(data[::-1])