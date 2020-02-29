"""
'r':read    'w':write   'x':write when file exist
'a':write next to the end of file   'b': binary model
't': text model     '+': write and read
"""


def file_operation():
    fs_list = []
    try:
        with open('test.txt', 'w+', encoding='utf-8') as f:
            f.write("I love U")
            f.write('\n')
            for i in range(1,24):
                f.write(str(i))     # write in line
                f.write('\n')       # manually blank line
            # add the '\n' into content to blank line
            f.writelines('hello , world! \n bye')
        f.close()
        with open('test.txt', 'r+') as f:
            # read every line of file, return list
            words = f.readlines()
            print(words)
    except IOError as ex:
        print(ex)
        print('write error!')
    finally:
        for fs in fs_list:
            fs.close()
    print('Done!')


if __name__ == '__main__':
    file_operation()