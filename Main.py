class Truck:
    def __init__(self, name):
        self.name = name

class HashChain:
    def __init__(self, initial_capacity = 10):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    def insert(self, key, item):
        bucket = hash(key)% len(self.table)
        bucket_list = self.table[bucket]
        #update key if it is already in the bucket
        for kv in bucket_list:
            #print key value
            if kv[0] == key: #if the key_value = key
                kv[1] = item #then update the value of key
                return True
        #if not, insert the item to the end of the bucket list
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    def search(self, key):
        bucket = hash(key)% len(self.table)
        bucket_list = self.table[bucket]

        for key_value in bucket_list:

            if key_value[0]== key:
                return key_value[1] #The value of key
        return None

    def remove(self, key):
        bucket = hash(key)% len(self.table)
        bucket_list = self.table[bucket]
        
        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])


myHash = HashChain()
packages = [
    [1, "123 Marmion Way"]
]
myHash.insert(packages[0][0], packages[0][1])
myHash.insert(2, "987 Goodbye Street")
print(myHash.table)