

characters = ['p', 'y', 't', 'h', 'o', 'n']
word = "".join(characters)
print(word)

def three():
    numbers = [30, 42, 28, 50, 15]
    for i, num in enumerate(numbers):
        # 使用 enumerate 迭代，给对象添加计数器，以枚举的形式返回
        print(i, num)

def use_zip():
    countries = ['France', 'Germany', 'Canada']
    capitals = ['Paris', 'Berlin', 'Ottawa']
    for country, capital in zip(countries,capitals):
      print(country, capital)