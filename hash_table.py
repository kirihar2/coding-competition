## Linear hash collision handling
class HashTable(): 

    def __init__(self):
        self.table = [False for i in range(27)]
        self.current_elements = 0 
        self.next_prime = 29
        self.k= 27
    def find_next_prime(self): 
        return self.next_prime * 2
        
    def resize(self):
        self.k = self.next_prime
        self.next_prime = self.find_next_prime()
        self.table += [False for i in range(self.next_prime-self.k)]
        
    def is_full(self):
        return self.current_elements < len(self.table)
    def add(self,element): 
        if self.is_full: 
            self.resize()
        hash = element.hash()
        hash_ind = hash % self.k
        while self.table[hash_ind] is not False:
            hash_ind = (hash + 1) % self.k
        self.table[hash_ind] = element
        self.current_elements += 1

## separate chaining for table for when size is undetermined
class HashTableChain():
    def __init__(self):
        pass