#We use a chaining hash table to organize our package data.
class HashChain:
    def __init__(self, initial_capacity = 10):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])
    #This will insert a new item with a key
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
    #This will search for an item by using it's key
    def search(self, key):
        bucket = hash(key)% len(self.table)
        bucket_list = self.table[bucket]

        for key_value in bucket_list:

            if key_value[0]== key:
                return key_value[1] #The value of key
        return None
    #This will remove an item by using it's key
    def remove(self, key):
        bucket = hash(key)% len(self.table)
        bucket_list = self.table[bucket]
        
        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])