class cat():
    def __init__(self):
        print("This is a cat!")

class dog(cat):
    def __init__(self, name='Dog'):
        print(f"This is a {name} ")  # 特殊输出方式
        super().__init__()
        self.name = name

if __name__ == '__main__':
    s = cat()
    d = dog()