class MyHashMap:
    # must string, it is about
    def __init__(self):
        # initialize the hash space
        self.size = 6
        self.map = [None] * self.size

    def _get_hash(self, key):
        # Build Your own Hash Function, which is the sum of ASCII of char % size
        myhash = 0
        for char in str(key):
            myhash += ord(char)
        return myhash % self.size

    def add(self, key, value):
        # Add what you want
        key_hash = self._get_hash(key)
        key_value = [key, value]    # point to hash value

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for each_pair in self.map[key_hash]:
                if each_pair[0] == key:
                    each_pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):
        # visit hashmap
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for each_pair in self.map[key_hash]:
                if each_pair[0] == key: return each_pair[1]
        return None

    def delete(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None: return False
        for i in range(0, len(self.map[key_hash])):
            if self.mao[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

    def print_hash(self):
        print('*** Hash Map Using Lists ***')
        for item in self.map:
            if item is not None:
                print(str(item))


if __name__ == '__main__':
    hs = MyHashMap()
    hs.add('S12z', 1111)
    hs.add('pete', '2222')
    hs.add('pete', '3333')  # overwrite
    hs.print_hash()
    print(hs.get('pete'))