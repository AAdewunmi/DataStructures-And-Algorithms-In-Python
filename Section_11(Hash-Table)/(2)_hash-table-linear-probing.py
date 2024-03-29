# Hash Table (Dealing with collisions using Linear Probing)
# =========================================================
# Linear probing is a scheme in computer programming for resolving collisions in hash tables, data structures for
# maintaining a collection of key–value pairs and looking up the value associated with a given key.
# It was invented in 1954 by Gene Amdahl, Elaine M. McGraw, and Arthur Samuel and first analyzed in 1963 by Donald Knuth.
#
# Along with quadratic probing and double hashing, linear probing is a form of open addressing. In these schemes,
# each cell of a hash table stores a single key–value pair. When the hash function causes a collision by mapping
# a new key to a cell of the hash table that is already occupied by another key, linear probing searches the table for
# the closest following free location and inserts the new key there. Lookups are performed in the same way, by searching
# the table sequentially starting at the position given by the hash function, until finding a cell with a matching key
# or an empty cell.
class HashTableLinearProbe:
    def __init__(self):
        self.hashtable_size = 10
        self.hashtable = [0] * self.hashtable_size

    # Hashing function
    def hashcode(self, key):
        return key % self.hashtable_size

    # Function to compute next index to insert element if index already
    # has an element stored in the Hash Table
    def lprobe(self, element):
        i = self.hashcode(element)
        j = 0
        while self.hashtable[(i + j) % self.hashtable_size] != 0:
            j = j + 1
        return (i + j) % self.hashtable_size

    # Function to insert elements into the Hash Table
    def insert(self, element):
        i = self.hashcode(element)
        if self.hashtable[i] == 0:
            self.hashtable[i] = element
        else:
            i = self.lprobe(element)
            self.hashtable[i] = element

    # Function to search for an element in the Hash Table
    def search(self, key):
        i = self.hashcode(key)
        j = 0
        while self.hashtable[(i + j) % self.hashtable_size] != key:
            if self.hashtable[(i + j) % self.hashtable_size] == 0:
                return False
            j = j + 1
        return True

    # Print contents of the table
    def display(self):
        print(self.hashtable)


H = HashTableLinearProbe()
H.insert(54)
H.insert(78)
H.insert(64)
H.insert(92)
H.insert(34)
H.insert(86)
H.insert(28)
H.display()
print('Search Result: ', H.search(34))