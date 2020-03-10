import os

filepath = 'D:\ss\ss'
filename = os.walk(filepath)

filename1 = os.listdir(filepath)



for i in filename1:
    print(i + " " )
print(type(filename), type(filename1))

