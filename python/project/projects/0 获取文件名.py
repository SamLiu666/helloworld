import os

filepath = 'D:\人工智能班级\线上课程\AI_photo'
filename = os.walk(filepath)

filename1 = os.listdir(filepath)


with open('list.txt', 'w+') as f:
    for i in filename1:
        f.write(i + '\n')

print(type(filename1))

