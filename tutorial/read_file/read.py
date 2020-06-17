file = open("test.txt", "r")
f = file.readlines()
print(f)
print(type(f))

string = "hello, good"
print(string.find("g"), string.find("9"))
print(string.count("l"), string.count("9"))

# print(f.find("g"), f.find("9")) list hanve no find
print(f.count("hello \n"), f.count("9"))