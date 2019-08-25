class Hashmap:

    def __init__(self, size=10):
        self.size = size
        self.map = [[] for _ in range(size)]

    def put(self, key, value):
        h = hash(key) % self.size
        bucket = self.map[h]
        tup = self.__get_tuple(key, bucket)
        if tup:
            bucket.remove(tup)
        bucket.append((key, value))

    def get(self, key):
        h = hash(key) % self.size
        return self.__get_value(key, self.map[h])

    def delete(self, key):
        h = hash(key) % self.size
        bucket = self.map[h]
        tup = self.__get_tuple(key, bucket)
        bucket.remove(tup)

    def __get_tuple(self, key, bucket):
        try:
            return next(filter(lambda el: el[0] == key, bucket))
        except StopIteration:
            return None

    def __get_value(self, key, bucket):
        tup = self.__get_tuple(key, bucket)
        return tup[1] if tup else None


if __name__ == '__main__':
    hm = Hashmap()
    hm.put("Wiktor", "Nissan super fast")
    hm.put("Anastasia", "Fiat 500")
    hm.put("Kacper", "Skoda")
    hm.put("Wiktor", "Ford")

    print(hm.map)

    print(hm.get("Anastasia"))
    print(hm.get("Wiktor"))
    print(hm.get("Wiktor2"))
    hm.delete("Anastasia")

    print(hm.get("Anastasia"))
