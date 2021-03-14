class Dict:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):
        # key 값에 hash 함수를 적용하여 배열의 길이로 나누어 index를 정하고
        # 이를 배열형태에 저장하여 가지고 있는다. 찾을 때는 역순으로..
        index = hash(key) % len(self.items)
        self.items[index] = value
        return
    
    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index]


    
my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))